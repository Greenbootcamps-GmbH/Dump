from idlelib.query import Query

from api import * # import the File FastAPI from the folder fastapi
from pydantic import BaseModel, Field, field_validator

#import fastapi -> Import the entire folder

app = FastAPI()

#change
# person_names = {
#     0 : "Carina Schoppe",
#     1 : "Bojan Mircheski",
#     2 : "Jasmin Schoppe",
#     3 : "Lukas Schoppe",
#     4 : "Hashim Schoppe",
#     5 : "Steve Schoppe",
#     6 : "John Schoppe",
#           }





class Adress(BaseModel):
    street: str = Field(..., title="The street of the person", description="The street of the person", max_length=25)
    housenumber: int = Field(..., title="The house number of the person", description="The house number of the person")
    city: str = Field(..., title="The city of the person", description="The city of the person", max_length=25)
    country: str = Field(..., title="The country of the person", description="The country of the person", max_length=25)

    # @field_validator ("housenumber")
    # def check_housenumber(self):
    #     if self.housenumber < 0:
    #         raise ValueError("The house number can not be negative")

class Person(BaseModel):
    name: str = Field(..., title="The name of the person", description="The name of the person", max_length=25)
    age: int = 25
    adress: Adress

person1 = Person(name="Carina Schoppe",
                 age=23,
                 adress=Adress(street="Hauptstraße",
                               housenumber=1,
                               city="Hamburg",
                               country="Germany"))

person_list = [person1]


print(person1.model_dump_json())

#
# @app.get("/person")
# def get_person(id: int = 5, street: str = None):
#     return {"name" : person_names[id]}

@app.get("/")
def read_root_element():
    return {"Hello" : "World"}

@app.get("/people")
def get_person(place: int =  Query(..., description="The place of the person", title="The place of the person")):
    return person_list[place]


@app.post("/people")
def put_person(name: str, age: int, street: str, housenumber: int, city: str, country: str):
    person = (
        Person(
            name=name,
            age=age,
            adress=Adress(
                street=street,
                housenumber=housenumber,
                city=city,
                country=country
            )
        )
    )
    person_list.append(person)
    return person



@app.get("/info")
def get_info():
    return {"Welcome to this World" : "Carinaa"}







#
#
# Create an API that is getting strings out of a list as well
# as putting strings into a list
#
# my_list = ["Hallo", "Worldf", "Carinma", "test"]
#












