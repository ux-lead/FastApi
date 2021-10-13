from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def speed():
    return {"message": "Hello World"}

@app.get("/home")
async def speed():
    return {"user": {
        "nome": "Renato",
        "CPF": ""
        }
        }