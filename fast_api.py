from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class User_input(BaseModel):
    operation: str
    x: float
    y: float

app = FastAPI()

@app.post("/calculate")
async def calc(user_input: User_input):
    return calculate(user_input.operation, user_input.x, user_input.y)

