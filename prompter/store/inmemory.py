import uuid
from prompter.store.base import BaseStore
from typing import List, Literal, Generic, TypeVar
from pydantic import BaseModel, Field

ResponseT = TypeVar('ResponseT', str, BaseModel)

class FewShots(BaseModel, Generic[ResponseT]):
    human_prompt: str
    response_example: ResponseT

class LLMParameters(BaseModel):
    max_tokens: int
    temperature: float
    top_p: float

class LLMModel(BaseModel):
    name: str
    type: Literal['openai', 'azure-openai', 'anthropic']
    api_version: str
    endpoint: str
    description: str
    parameters: LLMParameters

class ResponseSchemaExample(BaseModel):
    summary: str

class Prompt(BaseModel, Generic[ResponseT]):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()) + '_prompt')
    name: str = Field(default='name of prompt')
    description: str = Field(default='description of prompt')
    version: int = Field(default=1)
    model: LLMModel
    few_shots: FewShots[ResponseT]
    system_prompt: str
    human_prompt: str
    response_schema: type[ResponseT]

class InmemoryStore(BaseStore):
    def __init__(self) -> None:
        pass

p = Prompt(
    model=LLMModel(
        name='gpt-3.5-turbo',
        type='openai',
        api_version='v1',
        endpoint='https://api.openai.com',
        description='gpt-3.5-turbo',
        parameters=LLMParameters(
            max_tokens=100,
            temperature=0.7,
            top_p=0.9
        )
    ),
    few_shots=FewShots(
        human_prompt='Write a summary of the article.',
        response_example=ResponseSchemaExample(
            summary='The article is about the benefits of eating healthy.'
        )
    ),
    system_prompt='Write a summary of the article.',
    human_prompt='The article is about the benefits of eating healthy.',
    response_schema=ResponseSchemaExample
)
print(p.id)
