import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import messages_from_dict, messages_to_dict, AIMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder(variable_name="chat_history", n_messages=10),
        ("human", "{query}")
    ]
)

parser = StrOutputParser()

file_path="chat_history.json"
memory=[]

# read chat history from file
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        memory_data = json.load(f)
        memory = messages_from_dict(memory_data)

except FileNotFoundError: # create file if not exists 
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)


while True:
    query = input("You: ")
    if query == "exit()":
        break
    # final_messages = prompt.format_messages(chat_history=memory, query=query)
    # print(f"Number of messages sent to LLM: {len(final_messages)}")
    # for msg in final_messages:
    #     print(f"{type(msg).__name__}: {msg.content}")
    memory.append(HumanMessage(content=query))
    chain = prompt | llm | parser
    result = chain.invoke({"chat_history":memory, "query":query})
    memory.append(AIMessage(content=result))
    print(f"AI: {result}")
    print("*******************************")
    print(prompt.invoke({"chat_history":memory, "query":query}))
    print("*******************************")

# write list of messages back to chat history file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(messages_to_dict(memory), f, ensure_ascii=False, indent=2)
