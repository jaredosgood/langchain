from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


llm = OpenAI()
chat_model = ChatOpenAI()

# Predict a message
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm_prediction = llm.predict_messages(messages, temperature=1)
# >> Feetful of Fun
print("LLM: ", llm_prediction)

chat_prediction = chat_model.predict_messages(messages, temperature=1)
# >> Socks O'Color
print("Chat: ", chat_prediction)
