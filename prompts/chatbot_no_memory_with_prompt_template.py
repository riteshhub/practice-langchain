from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant"),
        ("human", "{query}")
    ]
)

parser = StrOutputParser()

while True:
    query = input("You: ")
    if query == "exit()":
        break
    chain = prompt | llm | parser
    result = chain.invoke({"query":query})
    print(f"AI: {result}")
    print("*******************************")
    print(prompt.invoke({"query": query}))
    print("*******************************")
