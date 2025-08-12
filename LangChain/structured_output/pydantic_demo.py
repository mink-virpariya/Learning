from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):

    name: str = "Dhananjay"
    age: Optional[int] = None
    email: EmailStr = "abc@gmail.com"
    cgpa: float = Field(ge=0, le=10, default=5.0, description='A decimal value representing the cgpa of the student.')

new_person = {'age': 27}
result = Person(**new_person)
print(result.model_dump()) # result is an pydantic object -> convert into dict/json