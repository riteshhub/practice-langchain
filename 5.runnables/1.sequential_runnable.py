# scenario - ask llm to provide list of 10 plant species of India, then ask llm to choose any plat at random and describe its characteristic
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt1 = PromptTemplate(
    template = "Provide list of 10 plant species of India"
)
prompt2 = PromptTemplate(
    template = "Choose random plant from {response} and desscibe it's characteristic",
    input_variables=["response"]
)

parser = StrOutputParser()

sequence = RunnableSequence(prompt1, llm, parser, prompt2, llm, parser)

result = sequence.invoke({})

print(result)
