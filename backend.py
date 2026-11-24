from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Arithmetic Operations API")


class Arthimetic(BaseModel):

    num1: int
    num2: int
    operation: str

@app.post("/")
def welcome():
    return {"message": "Arthimetic API is running"}

@app.post("/calculate")
async def calculate(request: Arthimetic):

    num1 = request.num1
    num2 = request.num2
    operation = request.operation.lower()
    

    if operation == "add":
        result = num1 + num2
    
    elif operation == "subtract":
        result = num1 - num2
        

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        result = num1 / num2

    else:
        print("The option you have given is invalid please select a proper one and try again")

    return {
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    }
        

