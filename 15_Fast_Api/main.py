from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()
app.counter = 0

class HelloResp(BaseModel):
    msg: str

class Product(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    code: str
    tax: Optional[float] = None


@app.get("/")
def root():
    return{"message": "Hello World"}

# @app.get("/hello/{name}")
# def hello_name(name: str):
#     return f"Hello {name.capitalize()}"

@app.get("/counter")
def count():
    app.counter += 1
    return {f"You visited this page: {app.counter} times."}

@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name.capitalize()}")