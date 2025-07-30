from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from opik.evaluation.metrics import ContextPrecision, ContextRecall, AnswerRelevance, Hallucination

load_dotenv()

# Map metric names to their classes
metrics = {
    "ContextPrecision": ContextPrecision(model="gemini/gemini-2.0-flash"),
    "ContextRecall": ContextRecall(model="gemini/gemini-2.0-flash"),
    "AnswerRelevance": AnswerRelevance(model="gemini/gemini-2.0-flash"),
    "Hallucination": Hallucination(model="gemini/gemini-2.0-flash")
}

# context_precision_metric = ContextPrecision(model="gemini/gemini-2.0-flash")
input="What is the capital of France?",
output="The capital of France is Paris. It is famous for its iconic Eiffel Tower and rich cultural heritage.",
expected_output="Paris",
context=["France is a country in Western Europe. Its capital is Paris, which is known for landmarks like the Eiffel Tower."]

results = {}

for name, metric in metrics.items():
    score = metric.score(
        input="What is the capital of France?",
        output="The capital of France is Paris. It is famous for its iconic Eiffel Tower and rich cultural heritage.",
        expected_output="Paris",
        context=["France is a country in Western Europe. Its capital is Paris, which is known for landmarks like the Eiffel Tower."]
    )
    results[name] = {
        "score": score.value,
        "reason": score.reason
    }

print("Evaluation Results:")
for metric_name, score in results.items():
    print(f"{metric_name}: {score}")

