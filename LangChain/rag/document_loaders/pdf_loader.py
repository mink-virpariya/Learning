from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Aspirin.pdf')
docs = loader.load()

print(docs[2])