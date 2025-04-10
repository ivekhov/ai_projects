"""

1. Appropriate action verbs
2. Detailed and precise instructions
3. Well-structured delimited prompts


1
write / complete/ explain / describe / propose / evaluate


2
- Provide specific, descriptive, and detailed instructions regarding:
- Context
- Output length
- Format and style 
- Audience


3
Use delimiters (parentheses, brackets, backticks, etc.) 
to specify input parts. Mention which delimiters are used


"""
# use f strings
text = "This is a sample text to summarize"
prompt = f"""Summarize the text delimited by triple backticks into bullet points.
        ```{text}```"""

print(prompt)

# or this: 
story = "In a distant galaxy, there was a brave space explorer named Alex."
prompt = f"""Complete the story delimited by triple backticks. ```{story}```"""

## func
from openai import OpenAI

client = OpenAI(api_key="api_key")


def get_response(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user",
            "content": prompt}],
            temperature = 0
            )
    return response.choices[0].message.content
##

##
# Create a request to complete the story
prompt = f"""Complete the given story delimited by triple backticks with only two paragraphs in the style of Shakespeare. ```{story}```"""


##




