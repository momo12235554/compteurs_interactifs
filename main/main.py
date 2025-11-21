from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

value = 0

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/value")
def read_value():
    return {"value": value}

@app.post("/update/{op}")
def modify_value(op: str):
    global value
    if op == "plus":
        value += 1
    elif op == "minus":
        value -= 1
    return {"value": value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
