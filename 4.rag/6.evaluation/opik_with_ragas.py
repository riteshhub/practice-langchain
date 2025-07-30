import asyncio
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from opik.integrations.langchain import OpikTracer

from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import Faithfulness, AnswerRelevancy, LLMContextPrecisionWithoutReference, LLMContextRecall
from ragas.llms import LangchainLLMWrapper

# Load environment variables
load_dotenv()

# Initialize Opik tracer (for monitoring and tracing)
opik_tracer = OpikTracer(project_name="practice_langchain")

# Initialize LLM with Opik tracer callback
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=1024,
    callbacks=[opik_tracer]
)

# Prompt template for question answering with contexts
prompt = PromptTemplate(
    template=(
        "You are the world's best instructor. Use the following pieces of retrieved context to answer "
        "the question in not more than 300 words. If you don't know the answer, just say that you don't know. "
        "Keep your answers concise and specific.\n\n"
        "Question: {question}\n"
        "Context: {context}\n"
        "Answer:"
    ),
    input_variables=['question', 'context']
)

# Output parser to get string response
parser = StrOutputParser()

# Setup vector store for retrieval
vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="sample",
    persist_directory="./.chroma_db"
)
retriever = vector_store.as_retriever(search_kwargs={'k': 3})

# Your user query
query = "What are the most effective strategies individuals can adopt at home to reduce environmental impact?"

# Step 1: Retrieval
docs = retriever.invoke(query)
context = '\n\n'.join(doc.page_content for doc in docs)

# Step 2: Augmentation + Generation pipeline
chain = prompt | llm | parser
result = chain.invoke({"question": query, "context": context}, callbacks=[opik_tracer])

# print("Generated Answer:\n", result)

# ---------- RAGAS EVALUATION ----------

# Create Ragas SingleTurnSample for evaluation
sample = SingleTurnSample(
    user_input=query,
    response=result,
    retrieved_contexts=[context],
    reference="Reduce energy use, minimize waste, use sustainable products, recycle, conserve water, and educate others."
)
llm_wrapper = LangchainLLMWrapper(llm)
# Initialize Ragas metrics
faithfulness = Faithfulness(llm=llm_wrapper)
answer_relevancy = AnswerRelevancy(llm=llm_wrapper, embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"))
context_precision = LLMContextPrecisionWithoutReference(llm=llm_wrapper)
context_recall = LLMContextRecall(llm=llm_wrapper)

# Async function to compute all metrics, passing OpikTracer to log evaluation traces
async def compute_all_metrics(sample):
    faithfulness_score = await faithfulness.single_turn_ascore(sample, callbacks=[opik_tracer])
    answer_relevancy_score = await answer_relevancy.single_turn_ascore(sample, callbacks=[opik_tracer])
    context_precision_score = await context_precision.single_turn_ascore(sample, callbacks=[opik_tracer])
    context_recall_score = await context_recall.single_turn_ascore(sample, callbacks=[opik_tracer])
    return {
        "faithfulness": faithfulness_score,
        "answer_relevancy": answer_relevancy_score,
        "context_precision": context_precision_score,
        "context_recall": context_recall_score
    }

# Run metric evaluation and print results
scores = asyncio.run(compute_all_metrics(sample))

print("\nRagas Evaluation Metrics:")
for metric_name, score in scores.items():
    print(f"{metric_name}: {score:.4f}")
