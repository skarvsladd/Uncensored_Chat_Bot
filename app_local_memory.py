import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1")
)


messages = [{'role': 'system', 'content': 'you are a helpful assistant'}]


while True:
    user_input = input("Prompt: ")
    
    messages.append({'role': 'user', 'content': user_input})
    

    response = client.chat.completions.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
        max_tokens=-1
    )

    print(response.choices[0].message.content)
    
    messages.append({'role': 'assistant', 'content': response.choices[0].message.content})




