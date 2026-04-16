from fastapi import FastAPI
from pydantic import BaseModel
from .calculator import sum, resta, multiply

app = FastAPI()

class OperationRequest(BaseModel):
    a: int
    b: int

@app.post("/sum")
def sum_endpoint(request: OperationRequest):
    result = sum(request.a, request.b)
    print("this is a dev test")
    return {"result": result}

@app.post("/resta")
def resta_endpoint(request: OperationRequest):
    result = resta(request.a, request.b)
    return {"result": result}

@app.post("/multiply")
def multiply_endpoint(request: OperationRequest):
    result = multiply(request.a, request.b)
    return {"result": result}