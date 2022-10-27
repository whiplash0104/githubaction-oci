from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Ya malio sal"}


@app.get("/name/{name}")
def hello_name(name: str):
    return {"Hello": name}
