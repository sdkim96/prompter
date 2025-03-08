
from typing import Optional
from collections import deque

from langchain.schema import BaseMessage, SystemMessage, AIMessage, HumanMessage

import prompter._types as _types

from prompter.message.messages import Messages
from prompter.utils import annotations, utils
from prompter.message.prompt import RawPrompt

class PrompterMessageBuilder:

    def __init__(
        self,
        promptlike: _types.PromptLike,
        prompt_seperator: _types.PromptSeperator,
        history: Optional[Messages] = None,
    ) -> None:
        utils.check_allowed_types(promptlike, _types.PromptLike)
        self.promptlike = promptlike
        self.prompt_seperator = prompt_seperator
        self.history = history if history else Messages()
        
        
    def _solve_string(
        self, 
        promptlike: str, 
        prompt_seperator: Optional[str],
        **kwargs    
    ) -> _types.FormattedPrompt:
        _system_user_pair= promptlike.split(prompt_seperator)
            
        #TODO: extract systemprompt to constants 
        try:
            _user_prompt: str= _system_user_pair[1]
        except IndexError:
            _user_prompt = "Answer the question."

        formatted_prompt = (   
            RawPrompt(system=_system_user_pair[0], user=_user_prompt)
            .format_placeholders(**kwargs)
        )
        return formatted_prompt


    @annotations.dev_log
    def build(self, **kwargs) -> Messages:
        if isinstance(self.promptlike, str):
            solved = self._solve_string(self.promptlike, self.prompt_seperator, **kwargs)
        elif isinstance(self.promptlike, list) and all(isinstance(item, dict) for item in self.promptlike):
            
            try:
                for item in self.promptlike:
                    if "role" in item and "content" in item:
                        if item["role"] == "system":
                            _system_prompt = item["content"]
                        
                        elif item["role"] == "user":
                            _user_prompt = item["content"]
                        else:
                            raise ValueError(f"Invalid role: {item['role']}")
            except KeyError:
                raise ValueError("Invalid prompt format. Key 'role' or 'content' is missing.")
            
            solved = RawPrompt(system=_system_prompt, user=_user_prompt).format_placeholders(**kwargs)
        
        elif isinstance(self.promptlike, _types.FormattedPrompt):
            solved = self.promptlike
        else:
            raise ValueError(f"Invalid prompt type: {type(self.promptlike)}")
        
        self.history.append(SystemMessage(solved[0]))
        self.history.append(HumanMessage(solved[1]))

        return self.history