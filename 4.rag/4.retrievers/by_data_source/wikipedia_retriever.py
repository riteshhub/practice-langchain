from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=4, lang="en", doc_content_chars_max=200)

docs = retriever.invoke("What are the developments for inclusion of Cricket in Olympics?")

print(docs)