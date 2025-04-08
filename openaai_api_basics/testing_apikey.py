import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('FIRST_OPENAI_API_KEY')


def main():
    client = OpenAI(
        api_key=API_KEY
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        # max_tokens=10,
        messages=[
            {
                "role": "user",
                "content": "In two sentences, how can the OpenAI API be used to upskill myself?"
            }
        ],
        temperature=0,
    )
    print(response.choices[0].message.content)


    response = client.moderations.create(
        model="text-moderation-latest",
        input="My favorite book is To Kill a Mockingbird."
    )

    # Print the category scores
    print(response.results[0].category_scores)    


if __name__ == "__main__":
    main()


