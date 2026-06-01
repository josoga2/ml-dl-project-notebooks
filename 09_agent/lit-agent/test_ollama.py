from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="qwen3:8b",
    messages=[
        {"role": "user",
         "content": "What is RNA sequencing?"}
    ]
)

print(response.choices[0].message.content)
