from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/home/mind/Mink/1.Learning/Langchain/rag/document_loaders/Aspirin.pdf')
docs = loader.load()


splitter = CharacterTextSplitter(chunk_size=500,
                                 chunk_overlap=0,
                                 separator=''
                                 )

result = splitter.split_documents(docs)
print(len(result))
print(result[0])
