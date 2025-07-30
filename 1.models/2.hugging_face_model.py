import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

os.environ["HF_HOME"] = "C:/Users/Ritesh_Patel/Documents/learning/AI/hugging_face_models"

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)

llm = ChatHuggingFace(llm=model, verbose=True)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)