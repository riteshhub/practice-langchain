## RAG
RAG stands for Retrieval-Augmented Generation, an advanced technique used to enhance large language models (LLMs) by integrating them with external and internal data sources in real time. Instead of only relying on the fixed training data of the model, RAG systems retrieve relevant facts or documents from databases, knowledge bases, or the internet to supplement their responses. This approach helps produce answers that are more accurate, contextually relevant, and up-to-date.

### Key advantages of RAG include:

* Access to current or domain-specific knowledge not present in the original training data.
* Improved factual accuracy and contextual relevance in responses.
* Reduced need for frequent and costly retraining of the language model.
* Enhanced transparency by allowing the inclusion of source references in outputs.

### Steps involved in building RAG

* Indexing - load external data to vector db
* Retrieval - fetch only relevant chunks from vector db based on user query.
* Augmentation - combining user query with relevant chunks and pass it as a context in the form of prompt to LLM model.
* Generation - get response from LLM model.