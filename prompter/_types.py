from collections import namedtuple
from typing import Union, Literal

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
