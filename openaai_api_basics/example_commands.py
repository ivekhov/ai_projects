# import client

def main():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=100,
    
        # Enter your prompt
        messages=[{"role": "user", "content": "In two sentences, how can the OpenAI API be used to upskill myself?"}]
    )

print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
