import os
import openai

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

# print(response)
print(response.choices[0].message.content)

