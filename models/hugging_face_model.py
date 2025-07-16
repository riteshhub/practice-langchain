import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

os.environ["HF_HOME"] = "C:\Users\Ritesh_Patel\Documents\learning\AI\hugging_face_models"

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm, verbose=True)

result = model.invoke(input="What are the most spoken languages in the world?")

print(result)