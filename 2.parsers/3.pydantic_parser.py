from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

class PlayerScore(BaseModel):
    name: str = Field(description="Name of the player")
    runs: int = Field(description="Total runs scored by player")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

parser = PydanticOutputParser(pydantic_object=PlayerScore)

prompt = PromptTemplate(
    template="Provide name and runs scored by {player} in ODI cricket \n{format_instruction}",
    input_variables=['player'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = prompt | llm | parser

result = chain.invoke({"player": "Virat Kohli"})

print(result)