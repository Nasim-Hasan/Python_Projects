import ollama

response = ollama.chat(
    model="granite3.3",
    messages=[
        {"role": "user", "content": "What is the temperature of Mars?"}
    ],
)

print(response["message"]["content"])
