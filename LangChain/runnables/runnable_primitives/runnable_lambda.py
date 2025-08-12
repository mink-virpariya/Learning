from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt1 = PromptTemplate(
    template="Write an toke on {topic} in one sentence.",
    input_variables=['topic']
)

parser = StrOutputParser()


def word_counter(text):
    return len(text.split())

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "total_words": RunnableLambda(word_counter)
    }
)

final_chain = RunnableSequence(joke_chain, parallel_chain)
result = final_chain.invoke({'topic', 'cricket'})
print(result)