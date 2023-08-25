from langchain import OpenAI, PromptTemplate


llm = OpenAI()

template = PromptTemplate(
   input_variables=["adjective", "content"],
   template="Tell me a {adjective} joke about {content}."
)

prompt = template.format(
   adjective="funny",
   content="chickens"
)

response = llm.generate(
   prompts=[prompt]
)

print(response)