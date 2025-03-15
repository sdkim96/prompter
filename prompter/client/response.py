from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, ClassVar

from prompter._types import Jsonable

class LLMResponse(BaseModel):
    """
    Information from the LLM response.
    """ # noqa: E501
    prompt_token_count: Optional[int] = Field(default=None, alias="promptTokenCount")
    response_token_count: Optional[int] = Field(default=None, alias="responseTokenCount")
    output: Jsonable
    stream_output: Optional[List[str]] = Field(default=None, alias="streamOutput")
    async_stream_output: Optional[List[str]] = Field(default=None, alias="asyncStreamOutput")
    __properties: ClassVar[List[str]] = ["promptTokenCount", "responseTokenCount", "output", "streamOutput", "asyncStreamOutput"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )
