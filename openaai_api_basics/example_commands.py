from openai import OpenAI

API_KEY = 'mykey'

def main():
    client = OpenAI(
        api_key=API_KEY
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=100,
    
        # Enter your prompt
        messages=[
            {
                "role": "user",
                "content": "In two sentences, how can the OpenAI API be used to upskill myself?"
            }
        ],

        # max_tokens: The maximum number of tokens to generate in the completion
        # На глаз: 1 токен ≈ 0.75 слова английского текста, в русском — плотность выше, около 1 токен ≈ 0.5-0.6 слова.
        # Онлайн: OpenAI Tokenizer
        # Python-библиотека: tiktoken 
        max_tokens=100,

        # Ranges from 0 (highly deterministic) to 2 (very random)
        temperature=0,
    
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

'''
- Investment involves committing money or capital to generate income or profit, 
with options like stocks, bonds, and real estate, requiring careful analysis and risk assessment.

- Diversifying investment portfolios helps minimize risk, making informed and diligent 
investing essential for wealth building and financial security.

'''