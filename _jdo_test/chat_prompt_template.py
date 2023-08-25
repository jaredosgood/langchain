from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# Format the messages
formatted_system_message = system_message_prompt.format_messages(input_language="English", output_language="French")
formatted_human_message = human_message_prompt.format_messages(text="I love programming.")

# Print the messages
print("System Message:", formatted_system_message)
print("Human Message:", formatted_human_message)
