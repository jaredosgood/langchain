from langchain import OpenAI, PromptTemplate

# Create a PromptTemplate with specified input variables and template string
template = PromptTemplate(
   input_variables=["adjective", "content"],
   template="Tell me a {adjective} joke about {content}."
)

# Format the template with specific values for the input variables
prompt = template.format(
   adjective="funny", 
   content="chickens"
)

# The variable 'prompt' now contains the string "Tell me a funny joke about chickens."
print(prompt)
