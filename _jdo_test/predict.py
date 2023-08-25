from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

text = "What would be a good company name for a company that makes colorful socks?"

result_llm = llm.predict(text)
print("Result from OpenAI:", result_llm)  # >> Feetful of Fun

result_chat_model = chat_model.predict(text)
print("Result from ChatOpenAI:", result_chat_model)  # >> Socks O'Color
