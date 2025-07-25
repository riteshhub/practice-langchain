from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader('.data/sample.docx')

docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)