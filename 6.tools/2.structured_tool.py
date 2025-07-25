from dotenv import load_dotenv
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

load_dotenv()


class MultiplyToolSchema(BaseModel):
    a: int = Field(description="first number to multiply")
    b: int = Field(description="second number to multiply")

def do_multiply(a:int, b:int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=do_multiply,
    name="multiply",
    description="multiply given numbers",
    args_schema=MultiplyToolSchema
)

print(multiply_tool.invoke({'a':3,'b':6}))