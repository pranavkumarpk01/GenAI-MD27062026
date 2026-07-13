from pydantic import BaseModel

class Verify (BaseModel):
    name:str
    age:int
    city:str