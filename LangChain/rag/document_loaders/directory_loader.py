from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)


# # Eager Loading
# docs = loader.load()
# for document in docs:
#     print(document.metadata)


# Lazy Loading
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
