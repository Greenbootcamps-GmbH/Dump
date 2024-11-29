from fastapi import FastAPI, Query
from pydantic import BaseModel, Field


class Parcel(BaseModel):
    id: int = Field(..., title="The id of the parcel", description="The id of the parcel", gt=0, le=100)
    name: str = Field(..., title="The name of the parcel", description="The name of the parcel", max_length=25)
    adress: str = Field(..., title="The adress of the parcel", description="The adress of the parcel", max_length=25)


parcel1 = Parcel(id=1, name="Carina", adress="Hamburg")
parcels = [parcel1]
app = FastAPI()

x = {0: "Carina"}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/parcel")
def read_parcel(index: int = Query(0, description="The index of the parcel", title="The index of the parcel", gt=0, le=100)):
    return parcels[index]

@app.post("/parcel")
def post_pacel(parcel: Parcel = Query(..., description="The parcel to add", title="The parcel to add")):
    parcels.append(parcel)
    return parcels[len(parcels) - 1]

@app.get("/test")
def read_test(index: int):
    return x[index]


@app.put("/test")
def read_test(index: int, value: str = Query(..., title="The value to replace")):
    x[index] = value
    return x[index]
