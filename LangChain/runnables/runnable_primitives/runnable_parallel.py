from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt1 = PromptTemplate(
    template="Create an LinkedIn post on: {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Create an Twitter post on: {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "lindekin": RunnableSequence(prompt1, model, parser),
    "tweet" : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'retrieval augmented generation (RAG)'})
print(result)