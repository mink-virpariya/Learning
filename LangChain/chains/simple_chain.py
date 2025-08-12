from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class OutputSchema(BaseModel):
    fact_1: str = Field('1st Fact of the given topic')
    fact_2: str = Field('2nd Fact of the given topic')
    fact_3: str = Field('3rd Fact of the given topic')
    fact_4: str = Field('4th Fact of the given topic')
    fact_5: str = Field('5th Fact of the given topic')

parser = PydanticOutputParser(pydantic_object=OutputSchema)

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

print(prompt)
print()

chain = prompt | model | parser
result = chain.invoke({'topic': 'cricket'})
pprint(result.model_dump())

chain.get_graph().print_ascii()