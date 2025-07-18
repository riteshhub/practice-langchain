from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

template = PromptTemplate.from_template("Tell me five characteristics of {plant}")

parser = StrOutputParser()

chain = template | llm | parser
result = chain.invoke({"plant": "mogra"})

print(result)