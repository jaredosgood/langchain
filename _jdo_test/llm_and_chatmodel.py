from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("hi!")
# >>> "Hi"

chat_model.predict("hi!")
# >>> "Hi"