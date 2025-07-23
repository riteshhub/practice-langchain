from typing import Type
from dotenv import load_dotenv
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

load_dotenv()

class MultiplyToolSchema(BaseModel):
    a: int = Field(description="first number to multiply")
    b: int = Field(description="second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "multiply given numbers"
    args_schema: Type[BaseModel] = MultiplyToolSchema

    def _run(self, a:int, b:int) -> int:
        return a*b
    
tool = MultiplyTool()

print(tool.invoke({'a': 5, 'b': 7}))