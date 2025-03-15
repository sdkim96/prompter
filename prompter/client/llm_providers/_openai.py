import os
import openai
import functools

from openai.types import chat as chatT
from typing import Optional, Union, List, cast

import prompter._types as _types

from prompter.message.messages import Messages
from prompter.client.response import LLMResponse

class OpenAIClientWrapper:

    def __init__(
        self, 
        model: str,
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        stream_mode: bool = False,
    ) -> None:
        
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI API key must be provided")
        
        self.api_key =api_key
        self.model = model
        self.model = model
        self.temperature = temperature
        self.stream_mode = stream_mode

    def __call__(
        self, 
        messages: Messages, 
        response_schema: _types.Jsonable
    ) -> LLMResponse:
        
        messages_to_call = messages.to_dict()

        _client = openai.OpenAI(api_key=self.api_key)
        call = self._build_function(
            _client, 
            messages_to_call, 
            response_schema, 
            self.stream_mode
        )
        
        completion: (
            chatT.ChatCompletion | 
            chatT.ParsedChatCompletion | 
            openai.Stream[chatT.ChatCompletionChunk]
        ) = call()
        
        return self._afterprocess(completion)


    def _afterprocess(
        self, 
        completion: Union[
            chatT.ChatCompletion, 
            chatT.ParsedChatCompletion, 
            openai.Stream[chatT.ChatCompletionChunk]
        ],
    ) -> LLMResponse:

        output: _types.Jsonable = ""
        stream_output: Optional[List[str]] = None
        input_t: int = 0
        output_t: int = 0

        if self.stream_mode:
            completion = cast(openai.Stream[chatT.ChatCompletionChunk], completion)
            
            stream_output = []
            for chunk in completion:

                if chunk.usage is not None:
                    input_t = chunk.usage.prompt_tokens
                    output_t = chunk.usage.completion_tokens

                if chunk.choices[0].delta.content is not None:
                    stream_output.append(chunk.choices[0].delta.content)
            
            stream_output.append('[NONE]')

        else:
            completion = cast(chatT.ChatCompletion | chatT.ParsedChatCompletion, completion)
            if completion.usage is not None:
                input_t = completion.usage.prompt_tokens
                output_t = completion.usage.completion_tokens

            resp = completion.choices[0].message.content
            if isinstance(completion, chatT.ParsedChatCompletion):
                resp = completion.choices[0].message.parsed

            if not resp:
                output = "No output"
            else:
                output = resp

        return LLMResponse(
            promptTokenCount=input_t,
            responseTokenCount=output_t,
            output=output,
            streamOutput=stream_output if self.stream_mode else None
        )

    def _build_function(
        self, 
        _client: openai.OpenAI, 
        messages, 
        response_schema,
        stream_mode: bool
    ):
        if response_schema != str:
            return functools.partial(
                _client.beta.chat.completions.parse, 
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                response_format=response_schema
            )
        else:
            if stream_mode:
                return functools.partial(
                    _client.chat.completions.create, 
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    stream=True
                )
            return functools.partial(
                _client.chat.completions.create, 
                model=self.model,
                messages=messages,
                temperature=self.temperature,
            )