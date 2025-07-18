from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

class Post(BaseModel):
    summary: str = Field(description="A brief summary of the post")
    sentiment: str = Field(description="sentiment as positive, negative or neutral")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

formatted_llm = llm.with_structured_output(Post)

result = formatted_llm.invoke(input="Increasing mobile phone use has a bad impact on children, exposing them to harmful content and impairing their focus. Mobile phones can waste a lot of time and sometimes feel like they tie me down rather than free me. Phones give much more room to conceal things, which can negatively affect family cohesion. Excessive screen time and phone addiction lead to health issues and lack of physical activity. I have had bad experiences in public transport where constant phone use disturbed others, showing a social downside.")

print(result)