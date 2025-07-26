from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from ragas.evaluation import evaluate
from ragas.dataset_schema import SingleTurnSample, EvaluationDataset

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024
)

prompt = PromptTemplate(
    template="""You are the world's best instructor. Use the following pieces of retrieved context to answer the question in not more than 300 words. If you don't know the answer, just say that you don't know. Keep your answers concise and specific.
    Question: {question} 
    Context: {context} 
    Answer:""",
    input_variables=['question', 'context']
)

parser = StrOutputParser()

vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="sample",
    persist_directory="./.chroma_db"
)

retriever = vector_store.as_retriever(search_kwargs={'k': 3})

query = "What are the most effective strategies individuals can adopt at home to reduce environmental impact?"

# retrieval
docs = retriever.invoke(query)

context = '\n\n'.join(doc.page_content for doc in docs)

# augmentation and generation
chain = prompt | llm | parser

result = chain.invoke({"question":query, "context":context})

print(result)

# Prepare evaluation data
sample = SingleTurnSample(
    user_input=query,
    retrieved_contexts=[context],
    response=result,
    reference="Reduce energy use, minimize waste, use sustainable products, recycle, conserve water, and educate others."
)

try:
    dataset = EvaluationDataset.from_list([sample.model_dump()])  # <-- pass a list of dicts

    # Evaluate using ragas
    eval_result = evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
        llm=llm,
        embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    )

    print(eval_result)
except:
    pass