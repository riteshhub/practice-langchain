# RAG
RAG stands for **Retrieval-Augmented Generation**, an advanced technique used to enhance large language models (LLMs) by integrating them with external and internal data sources in real time. Instead of only relying on the fixed training data of the model, RAG systems retrieve relevant facts or documents from databases, knowledge bases, or the internet to supplement their responses. This approach helps produce answers that are more accurate, contextually relevant, and up-to-date.

### Key advantages of RAG include:

* Access to current or domain-specific knowledge not present in the original training data.
* Improved factual accuracy and contextual relevance in responses.
* Reduced need for frequent and costly retraining of the language model.
* Enhanced transparency by allowing the inclusion of source references in outputs.

### Steps involved in building RAG

* **Indexing** - load external data to vector db
* **Retrieval** - fetch only relevant chunks from vector db based on user query.
* **Augmentation** - combining user query with relevant chunks and pass it as a context in the form of prompt to LLM model.
* **Generation** - get response from LLM model.

## Document Loader
Support various file formats with unified structure and methods.
https://python.langchain.com/docs/integrations/document_loaders/

## Text Splitters
Multiple strategy based on 
* Length of the document
* Stucture of the document - paragraph, lines
* Specific language document - markdown, python, java

https://python.langchain.com/docs/concepts/text_splitters/


## Vector Store
https://python.langchain.com/docs/integrations/vectorstores/

## Retrievers
Multiple startegies to fetch data based on
* data source - wikipedia, chromadb .. 
* search strategy - mmr, multi query ..

https://python.langchain.com/docs/integrations/retrievers/

#### 1. Maximum Marginal Relevance (MMR)
---

> How can we pick results that are not only relevant to the query but also different from each other?

MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.

<u> Why MMR Retriever ? </u>

In regular similarity search, you may get documents that are:

* All very similar to each other
* Repeating the same info
* Lacking diverse perspectives

MMR Retriever avoids that by:

* Picking the most relevant document first.

* Then picking the next most relevant and least similar to already selected docs.

This helps especially in RAG pipelines where, you want your context window to contain diverse but still relevant information


#### 2. Multi Query Retriever
---
A Multi-Query Retriever is an advanced retrieval technique used mainly in Large Language Model (LLM) based systems to improve the quality and diversity of documents retrieved for a single input query.

> Sometimes a user query might not capture all the ways information is phrased in your documents. 

Here's how it works:

1. Instead of using just one query to search a document database or vector store, the Multi-Query Retriever uses an LLM (like GPT) to automatically generate multiple variations or perspectives of the original query.

2. It then runs each of these queries independently through the retriever system to fetch relevant documents for each.

3. Finally, it combines the results by taking the unique union of all retrieved documents, which results in a larger and more diverse set of documents that better cover the intent behind the original query.

> **Scenario**: A user asks, "How can I reset my password?"
<br> Multi-Query Retriever generates multiple queries like:
<br> _"Steps for password reset"_
<br> _"Forgot password instructions"_
<br> _"Account recovery process"_
<br> This retrieves various help articles, FAQs, and policy documents, ensuring the user gets complete and relevant guidance, even if the original query had missing or ambiguous terms.

#### 3. Contextual Compression Retriever
---
It improves retrieval quality by compressing documents after retrieval, keeping only the relevant content based on the user's query.

##### ❓Query:
**"What is photosynthesis?"**

##### 📝 Retrieved Document (by a traditional retriever):

> "The Grand Canyon is a famous natural site.  
> Photosynthesis is how plants convert light into energy.  
> Many tourists visit every year."

##### ❌ **Problem:**
- The retriever returns the **entire paragraph**
- Only **one sentence** is actually relevant to the query
- The rest is **irrelevant noise** that wastes context window and may co

##### ✅ What Contextual Compression Retriever does:

> Returns only the relevant part, e.g.  
> "Photosynthesis is how plants convert light into energy."

##### ⚙️ How It Works

1. **Base Retriever** (e.g., FAISS, Chroma) retrieves N documents.
2. A **compressor** (usually an LLM) is **applied to each document**.
3. The compressor **keeps only the parts relevant to the query.**
4. Irrelevant content is discarded.

##### ✅ When to Use

- Your documents are **long and contain mixed information**
- You want to **reduce context length** for LLMs
- You need to **improve answer accuracy** in RAG pipelines