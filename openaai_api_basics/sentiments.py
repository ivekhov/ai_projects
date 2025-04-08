client = OpenAI(api_key="<OPENAI_API_TOKEN>")


# sentiments

# Define a multi-line prompt to classify sentiment
prompt = """Classify sentiment as negative, positive, or neutral in the following statements:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=100
)

print(response.choices[0].message.content)


## categorization
# Define a prompt for the categorization
prompt = "Categorize the following companies: Apple, Microsoft, Saudi Aramco, Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, LVMH"

# Define a prompt for the categorization
prompt = "Categorize the following companies on four categories Tech, Energy, Luxury Goods, or Investment: Apple, Microsoft, Saudi Aramco, Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, LVMH"

