from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from opik.integrations.langchain import OpikTracer

load_dotenv()

opik_tracer = OpikTracer(project_name="practice_langchain")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024,
    callbacks=[opik_tracer]
)
prompt_template = PromptTemplate(
    input_variables=["input"], template="Write a haiku about {input}"
)
llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "AI engineering"}, callbacks=[opik_tracer]))
