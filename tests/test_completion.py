from pydantic import BaseModel

from prompter.completion import OpenAICompletion

class Resp(BaseModel):
    content: str

def test_openai_completion():
    response_schema = [str, Resp]
    returns = []
    for sch in response_schema:
        comp = (
            OpenAICompletion(
                comp_id='1',
                comp_type='openai',
                comp_name='GPT-3',
                prompt=[
                    {'role': 'system', 'content': 'Hello, my name is. {name}'}, 
                    {'role': 'user', 'content': 'What is your name?'}
                ],
            )
            .build_prompt(name="sdkim")
            .infer(response_schema=sch)
        )
        returns.append(comp)

    comp = (
        OpenAICompletion(
            comp_id='1',
            comp_type='openai',
            comp_name='GPT-3',
            prompt=[
                {'role': 'system', 'content': 'Hello, my name is. {name}'}, 
                {'role': 'user', 'content': 'What is your name?'}
            ],
            stream_mode=True
        )
        .build_prompt(name="sdkim")
        .infer(response_schema=str)
    )
    returns.append(comp)

    print(returns)


if __name__ == '__main__':
    test_openai_completion()