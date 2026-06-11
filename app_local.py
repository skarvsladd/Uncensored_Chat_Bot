import os
import openai

openai.api_type = os.getenv("OPENAI_API_TYPE", "open_ai")
openai.api_base = os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1")
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': 'you are a helpful assistant'},
        {'role': 'user', 'content': 'What is the capital of France?'}
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response)
print(response.choices[0].message.content)

