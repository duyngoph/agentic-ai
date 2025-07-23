from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "developer", 
            "content": "You are a helpful assistant."
        },
        {
            "role": "user", 
            "content": "Tell me a joke about programming."
        },
    ],
)
print(response.output_test)