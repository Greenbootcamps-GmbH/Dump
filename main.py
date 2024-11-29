from fastapi import FastAPI # import the File FastAPI from the folder fastapi
from pydantic import BaseModel, Field, validator, field_validator

#import fastapi -> Import the entire folder

app = FastAPI()

#change
# person_names = {
#     0 : "Carina Schoppe",
#     1 : "Bojan Mircheski",
#     2 : "Jasmin Schoppe",
#     3 : "Lukas Schoppe",
#     4 : "Florian Schoppe",
#     5 : "Andreas Schoppe",
#           }

class Adress(BaseModel):
    street: str = Field(..., max_length=50)
    city: str = Field(..., max_length=50)
    country: str = Field(..., max_length=50)
    zip: str = Field(..., max_length=50)
    housenumber: int = Field(..., gt=0, le=100)


class Person(BaseModel):
    name: str = Field(..., title="The name of the person", max_length=50)
    age: int = Field(..., gt=0, le=100, description="Age of the person")
    nice: bool = True
    adress: Adress



person_list = []

person1 = Person(name="Carina Schoppe", age=25, nice=True,adress= Adress(street="Dorpsstraat", city="Gent", country="Belgium", zip="9000", housenumber=1))

print(person1.model_dump_json())

#
# @app.get("/person")
# def get_person(id: int = 5, street: str = None):
#     return {"name" : person_names[id]}

@app.get("/")
def read_root_element():
    return {"Hello": "World"}


@app.get("/info")
def get_info():
    return {"Welcome to this World" : "Carinaa"}

