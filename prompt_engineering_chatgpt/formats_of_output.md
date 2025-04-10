## TABLE

prompt = """Generate a table containing 5 movies I should watch if I am an action
lover, with columns for Title and Rating."""


## LISTS
 
prompt = "Generate a list containing the names of the top 5 cities to visit."

prompt = "Generate an unordered list containing the names of the top 5 cities to visit."

## Structured paragraphs

prompt = "Provide a structured paragraph with clear headings and subheadings about the benefits of regular exercise on overall health and well-being."


## Combination of instructions

```python

# Create the instructions
instructions = """
You will be provided with a text delimited by triple backticks.
Determine the language and generate a suitable title for it. 
"""

# Create the output format
output_format = "Include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line."

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"

response = get_response(prompt)
```


Another example
```python
# Create the instructions
instructions = """You will be provided with a text delimited by triple backticks. Determine the language and number of sentences. If the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title."""

# Create the output format
output_format = """Include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line."""

prompt = instructions + output_format + f"```{text}```"

```
Response
"""Text: The sun was setting behind the mountains, casting a warm golden glow across the landscape.  
Language: English  
Number of sentences: 1  
Title: N/A  
"""

