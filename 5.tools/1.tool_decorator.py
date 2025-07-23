from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    "multiply given numbers"
    return a*b

print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema()) # this is what being send to LLM about tool, to understand its capability and requirement

print("Response: ",multiply.invoke({'a':3, 'b':7}))