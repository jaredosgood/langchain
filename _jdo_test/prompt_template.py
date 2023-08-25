from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
formatted_prompt = prompt.format(product="colorful socks")

# Print the formatted prompt
print("Prompt:", formatted_prompt)
