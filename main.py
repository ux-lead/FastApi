from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def speed_0():
    return {"message": "Hello World"}

@app.get("/home")
async def speed_1():
    return {"user": {
        "nome": "Renato",
        "CPF": ""
        }
        }