from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    "multiply given numbers"
    return a*b

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

llm_with_tools = llm.bind_tools([multiply])

# result = llm_with_tools.invoke("How are you?")
result = llm_with_tools.invoke("perform multiplication of 5 with 6")

if hasattr(result, "tool_calls"):
    result = multiply.invoke(result.tool_calls[0])

print(result.content)