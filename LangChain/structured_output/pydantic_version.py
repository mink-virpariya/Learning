from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class OutputSchema(BaseModel):

    key_themes: list[str] = Field(description='write down all the key themes discussed in the review in a list')
    summary: str = Field(description='Return the summary of the review')
    sentiment: Literal['Positive, Negative', 'Netural'] = Field(description='Return the sentiment of the review, either positive, negative or netural')
    pros: Optional[list[str]] = Field(description='Return all the pros of the review in a list')
    cons: Optional[list[str]] = Field(description='Return all the cons of the review in a list')

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
structured_model = model.with_structured_output(OutputSchema)

prompt = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh"""

result = structured_model.invoke(prompt)
print(result.model_dump())
