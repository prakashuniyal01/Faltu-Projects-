from openai import OpenAI

# apikey = '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'

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)