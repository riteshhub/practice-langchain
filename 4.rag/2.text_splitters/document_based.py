from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('.data/sample.pdf')
docs = loader.load()

text = """
    def __init__(self, provider):
        self.provider = provider
        self.vector_store = self._get_vector_store()

    def _get_vector_store(self):
        if self.provider == 'aws':
            logger.info(f"Using configured LLM provider: {self.provider}")
            return AWSVectorStore(filename=self.filename, uploaded_by_user=self.user)
        if self.provider == 'azure':
            return AzureVectorStore(filename=self.filename, uploaded_by_user=self.user)
        if self.provider == 'open_source':
            return OpenSourceVectorStore()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=100,
    chunk_overlap=0,
    language=Language.PYTHON
)

doc_chunks = splitter.split_documents(documents=docs)
text_chunks = splitter.split_text(text=text)

print(f"docs - first chunk data {doc_chunks[0]}")
print(f"docs - first chunk lenght {len(doc_chunks[0].page_content)}")
print(f"text - first text data {text_chunks[0]}")
print(f"text - first text length {len(text_chunks[0])}")