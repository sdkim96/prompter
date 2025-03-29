import abc
from typing import Optional, Literal

import prompter._types as _types

from prompter.store import BaseStore, InmemoryStore
from prompter.message.builder import PrompterMessageBuilder
from prompter.message.messages import Messages
from prompter.client.llm_providers._openai import OpenAIClientWrapper


class BaseCompletion(abc.ABC):

    def __init__(
        self,
        comp_id: str,
        comp_type: _types.CompletionType,
        comp_name: str,
        model: str,
    ) -> None:
        self.comp_id = comp_id
        self.comp_type = comp_type
        self.comp_name = comp_name
        self.model = model

    @abc.abstractmethod
    def infer(self):
        """동기 방식 추론 메서드 (각 자식 클래스에서 반드시 구현해야 함)"""
        pass


class OpenAICompletion(BaseCompletion):

    def __init__(
        self,
        *,
        comp_id: str,
        comp_type: _types.CompletionType = "openai",
        comp_name: str,
        user_name: str,
        prompt: _types.PromptLike,
        prompt_seperator: _types.PromptSeperator = '[user]',
        model: Literal["gpt-4o", "gpt-4o-mini"] = "gpt-4o-mini",
        store: Optional[BaseStore] = None,
        stream_mode: bool = False,
        use_multi_turn: bool = False,
    ) -> None:
        """ prompt can be beforeparametrized string, list of dictionaries or FormattedPrompt """
        super().__init__(comp_id, comp_type, comp_name, model)

        self.stream_mode = stream_mode
        if use_multi_turn:
            if store is None:
                self.store = InmemoryStore()

            self.store.get_history(
                comp_id=comp_id
            )

        # private
        self._message_builder = PrompterMessageBuilder(
            promptlike=prompt, 
            prompt_seperator=prompt_seperator,
            history=history
        )

        self._messages = None
        self._client= OpenAIClientWrapper(
            model=self.model,
            stream_mode=self.stream_mode
        )

    @property
    def ready_to_infer(self):
        return self._messages is not None
    
    def build_prompt(self, **kwargs):
        """OpenAI 모델을 사용한 동기 방식 추론"""
        messages = self._message_builder.build(**kwargs)
        self._messages = messages

        return self
    
    def infer(
        self,
        response_schema: type[_types.Jsonable] = str,
    ):
        """OpenAI 모델을 사용한 동기 방식 추론"""
        if not self.ready_to_infer:
            raise ValueError('You must build prompt before infer')

        return self._client(self._messages, response_schema) # type: ignore