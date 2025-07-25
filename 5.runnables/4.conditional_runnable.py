from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant that personalizes marketing messages."),
    ("human", "{message}")
])

parser = StrOutputParser()

def message_by_age(user):
    if user["age"] < 18:
        return f"Write an enthusiastic message for a teenager named {user['name']} about our new teen collection."
    elif user["age"] < 30:
        return f"Write a trendy message for a young adult named {user['name']} about our latest outfits."
    else:
        return f"Write a professional message for an adult named {user['name']} about our premium range."

branch = RunnableBranch(
    (lambda x: x["age"] < 18, RunnableLambda(message_by_age)),
    (lambda x: 18 <= x["age"] < 30, RunnableLambda(message_by_age)),
    RunnableLambda(message_by_age)
)

personalized_message_chain = branch | prompt | llm | parser

result = personalized_message_chain.invoke({"name": "Alice", "age": 65})
print(result)
