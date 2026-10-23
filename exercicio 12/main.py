from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API no ar"}


@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}
