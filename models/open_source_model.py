from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.2",
    temperature=0.1,
    max_output_tokens=1024
)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)