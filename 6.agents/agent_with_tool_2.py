import warnings
import yfinance as yf
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
# from pydantic import BaseModel

warnings.filterwarnings(action="ignore")

load_dotenv()

@tool
def get_stock_price(input: str) -> float:
    "get the latest price of given stock"
    ticker = yf.Ticker(input)
    todays_data = ticker.history(period="1d", interval="1m")
    current_price = todays_data["Close"].iloc[-1]
    return current_price

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = hub.pull("hwchase17/react") # pulls the react prompt from https://smith.langchain.com/hub

my_agent = create_react_agent(
    llm=llm,
    tools=[get_stock_price],
    prompt=prompt
)

my_executor = AgentExecutor(
    agent=my_agent,
    tools=[get_stock_price],
    verbose=True,
    handle_parsing_errors=True
)

# result = my_executor.invoke({"input":"Hi how are you?"})
result = my_executor.invoke({"input":"what is the latest price of stock ITC.BO"})

print(result['output'])