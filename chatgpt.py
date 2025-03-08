from openai import OpenAI

with open("api_key") as f:
    api_key = f.read()

client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
