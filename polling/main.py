from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

value = 0

BASE = os.path.dirname(__file__)
STATIC = os.path.join(BASE, "static")

app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC, "index.html"))

@app.get("/value")
def read_value():
    return {"value": value}

@app.post("/change/{mode}")
def change_value(mode: str):
    global value
    if mode == "up":
        value += 1
    elif mode == "down":
        value -= 1
    return {"value": value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("polling.main:app", host="127.0.0.1", port=8001, reload=True)
