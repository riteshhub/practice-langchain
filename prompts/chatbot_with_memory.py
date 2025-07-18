from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

memory=[]
while True:
    query = input("You: ")
    memory.append(query)
    if query == "exit()":
        break
    response = llm.invoke(memory)
    memory.append(response.content)
    print("AI: ", response.content)