from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket_poem.txt')
docs = loader.load()

print(docs)