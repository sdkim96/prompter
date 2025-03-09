import os
import openai
from typing import AsyncGenerator, Optional

from prompter.message.messages import Messages
from prompter.utils.annotations import dev_log
from prompter.provider.base import BaseLLMClientWrapper

class OpenAIClientWrapper(BaseLLMClientWrapper):

    def __init__(
        self, 
        api_key: Optional[str] = None,
        model: str = "gpt-4",
        temperature: float = 0.7,
        stream_mode: bool = False,
        async_mode: bool = False,
    ) -> None:
        
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI API key must be provided")
        
        super().__init__(api_key, stream_mode, async_mode)
        self.model = model
        self.temperature = temperature

    @dev_log
    def invoke(self, messages: Messages, **kwargs) -> str:
        """ 동기 방식으로 OpenAI API 호출 """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages.to_dict(),
            temperature=self.temperature,
            **kwargs
        )
        return response["choices"][0]["message"]["content"]

    @dev_log
    async def ainvoke(self, messages: Messages, **kwargs) -> str:
        """ 비동기 방식으로 OpenAI API 호출 """
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=messages.to_dict(),
            temperature=self.temperature,
            **kwargs
        )
        return response["choices"][0]["message"]["content"]

    @dev_log
    def stream(self, messages: Messages, **kwargs) -> str:
        """ 동기 스트리밍 방식으로 OpenAI API 호출 """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages.to_dict(),
            temperature=self.temperature,
            stream=True,
            **kwargs
        )
        return "".join(chunk["choices"][0]["delta"].get("content", "") for chunk in response)

    @dev_log
    async def astream(self, messages: Messages, **kwargs) -> AsyncGenerator[str, None]:
        """ 비동기 스트리밍 방식으로 OpenAI API 호출 """
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=messages.to_dict(),
            temperature=self.temperature,
            stream=True,
            **kwargs
        )
        async for chunk in response:
            yield chunk["choices"][0]["delta"].get("content", "")