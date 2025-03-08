import abc
from typing import Optional

import prompter._types as _types

from prompter.message.builder import PrompterMessageBuilder
from prompter.message.messages import Messages


class BaseCompletion(abc.ABC):

    def __init__(
        self,
        comp_id: str,
        comp_type: str,
        comp_name: str,
    ) -> None:
        self.comp_id = comp_id
        self.comp_type = comp_type
        self.comp_name = comp_name

    @abc.abstractmethod
    def infer(self):
        """동기 방식 추론 메서드 (각 자식 클래스에서 반드시 구현해야 함)"""
        pass

    @abc.abstractmethod
    async def ainfer(self):
        """비동기 방식 추론 메서드 (각 자식 클래스에서 반드시 구현해야 함)"""
        pass


class OpenAICompletion(BaseCompletion):

    def __init__(
        self,
        *,
        comp_id: str,
        comp_type: str,
        comp_name: str,
        prompt: _types.PromptLike,
        prompt_seperator: _types.PromptSeperator = '[user]',
        history: Optional[Messages] = None,
    ) -> None:
        """ prompt can be beforeparametrized string, list of dictionaries or FormattedPrompt """
        super().__init__(comp_id, comp_type, comp_name)
        self._message_builder = PrompterMessageBuilder(
            prompt, 
            prompt_seperator,
            history
        )

    def infer(self, **kwargs):
        """OpenAI 모델을 사용한 동기 방식 추론"""
        messages = self._message_builder.build(**kwargs)
        print(messages)

    async def ainfer(self):
        """OpenAI 모델을 사용한 비동기 방식 추론"""


if __name__ == '__main__':
    OpenAICompletion(
        comp_id='1',
        comp_type='openai',
        comp_name='GPT-3',
        prompt=[{'role': 'system', 'content': 'Hello, my name is.'}, {'role': 'user', 'content': 'gogo {gogo} sgaga {sgaga}'}],
    ).infer(name="gogo", gogo="gogo", sgaga="sgaga")