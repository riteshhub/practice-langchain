import warnings
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
# from pydantic import BaseModel

warnings.filterwarnings(action="ignore")

load_dotenv()

# class MultiplyInput(BaseModel):
#     a: int
#     b: int

# @tool(args_schema=MultiplyInput)
# def multiply(a: int, b: int) -> int:
#     """Multiply given numbers."""
#     return a * b

@tool
def multiply(input: str) -> int:
    """Multiply two numbers provided as a comma-separated string."""
    a, b = map(int, input.split(","))
    return a * b

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = hub.pull("hwchase17/react") # pulls the react prompt from https://smith.langchain.com/hub

my_agent = create_react_agent(
    llm=llm,
    tools=[multiply],
    prompt=prompt
)

my_executor = AgentExecutor(
    agent=my_agent,
    tools=[multiply],
    verbose=True,
    handle_parsing_errors=True
)

# result = my_executor.invoke({"input":"Hi how are you?"})
result = my_executor.invoke({"input":"how are you?"})

print(result['output'])