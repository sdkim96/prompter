from collections import deque
from typing import List
from prompter import _types

class Messages(deque[_types.Message]):  # 🔹 타입 명확히 지정

    def __init__(self) -> None:
        super().__init__()
        self._context: str = ""

    def to_dict(self) -> List[dict[str, str]]:  # 🔹 반환 타입을 명확히 지정
        result: List[dict[str, str]] = []

        for msg in self:
            what_to_post = msg.to_json().get('kwargs', {})
            role = what_to_post.get('type', '') 
            content = what_to_post.get('content', '') 

            result.append({'role': self._edit_role(role), 'content': content})

        return result

    def _edit_role(self, role: _types.MessageRoles):
        if role == 'system':
            return 'system'
        elif role == 'human':
            return 'user'
        elif role == 'ai':
            return 'assistant'
        else:
            return 'system'


    def inject_context(self, context: str) -> None:
        self._context = context