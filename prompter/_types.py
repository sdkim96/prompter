from collections import namedtuple
from typing import Union, Literal, TypeAlias
from pydantic import BaseModel

from langchain.schema import HumanMessage, SystemMessage, AIMessage
FormattedPrompt = namedtuple("FormattedPrompt", ["system", "user"])

PromptLike = Union[
    str,
    list[dict[str, str]],
    FormattedPrompt
]

PromptSeperator = Literal[
    "[user]",
    "[user_prompt]",
    "[사용자 메시지]"
]

Jsonable = Union[
    str,
    BaseModel,
]

Message = Union[
    HumanMessage, SystemMessage, AIMessage
]


MessageRoles: TypeAlias = Literal[
    'human',
    'system',
    'ai'
]