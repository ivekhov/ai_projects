# Подсказки для настройки модели


# для форматирования (например) ответа
# один пример

prompt =  """
 Q: Sum the numbers 3, 5, and 6. A: 3+5+6=14
 Q: Sum the numbers 2, 4, and 7. A:
 """
# model response will be: 2+4+7=13



# для контекста
# несколько примеров
prompt = """
Text: Today the weather is fantastic -> Classification: positive
Text: The furniture is small -> Classification: neutral
Text: I don't like your attitude -> Classification: negative
"""
# resp example: "negative"


prompt = """
Q: extract the odd numbers from the set {1, 3, 7, 12, 19}. A: {1, 3, 7, 19}
Q: extract the odd numbers from the set {3, 5, 11, 12, 16}. A: 
"""

# CHAT FORMAT
sponse = client.chat.completions.create(
  model = "gpt-4o-mini",

  # Provide the examples as previous conversations
  messages = [
    # education examples
    {"role": "user", "content": "The product quality exceeded my expectations"},
              {"role": "assistant", "content": "1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant", "content": "-1"},
              
    # new task
    {"role": "user", "content": "The price of the product is really fair given its features"}
    ],
  temperature = 0
)
print(response.choices[0].message.content)


# CODE validation

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""" Assess the function provided in the code delimited by triple backticks as follows:
Step 1. Check correctness of syntax.
Step 2. Receiving two inputs.
Step 3. Returning one output.
Code: ```{code}```. """


## MULTI STEPS (1)
# Explicitly tell model what to do (like by steps above)





## CHAINS OF THOUGHT (2)
# sending to model Questions and answers model learns from


example = """
Q: The odd numbers in this group add up to an even number:  9, 10, 13, 4, 2.
A: Adding all the odd numbers (9, 13) gives 22. The answer is True.
"""
question = """
Q: The odd numbers in this group add up to an even number: 15, 13, 82, 7.
A:
"""
prompt = example + question

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2. Adding them: 10+4+2=16. """

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}. 
              A:"""

# Create the final prompt
prompt = example + question



## Self-consistency prompting (3)

self_consistency_instruction = """
Imagine three completely independent experts who
reason differently are answering this question. The final answer is obtained by
majority vote. The question is: """


problem_to_solve = """
If there are 10 cars in the parking lot and 3 more cars arrive.
Half the original number of cars leave. Then, half of the current number of cars
arrive. How many cars are there in the parking? """

prompt = self_consistency_instruction + problem_to_solve

## 
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> No explicit emotion

They sat and ate their meal ->

"""


## 