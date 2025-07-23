from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchResults

tool = DuckDuckGoSearchResults()

print(tool.invoke("ayurveda presence outside India"))