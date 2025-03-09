from typing import Callable

from prompter.message.messages import Messages
from prompter.utils.annotations import dev_log

class BaseLLMClientWrapper:

    def __init__(
        self, 
        api_key: str,
        stream_mode: bool = False,
        async_mode: bool = False,
    ) -> None:
        self.api_key = api_key
        self.stream_mode = stream_mode
        self.async_mode = async_mode

    @dev_log
    def __call__(self, messages: Messages, **kwargs) -> str:

        method = self._choose_method()
        return method(messages, **kwargs)
    

    def _choose_method(self) -> Callable:
        if self.stream_mode:
            if self.async_mode:
                return self.astream
            else:
                return self.stream
        else:
            if self.async_mode:
                return self.ainvoke
            else:
                return self.invoke
    
    def invoke(self, messages: Messages, **kwargs) -> str:
        return "invoke"
    
    async def ainvoke(self, messages: Messages, **kwargs) -> str:
        return "ainvoke"
    
    def stream(self, messages: Messages, **kwargs) -> str:
        return "stream"
    
    async def astream(self, messages: Messages, **kwargs) -> str:
        return "astream"
