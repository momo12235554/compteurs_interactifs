from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

count = 0
clients = set()

BASE = os.path.dirname(__file__)
STATIC = os.path.join(BASE, "static")

app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.get("/")
async def home():
    return FileResponse(os.path.join(STATIC, "index.html"))


async def update_all():
    data = {"value": count}
    closed = []

    for ws in clients:
        try:
            await ws.send_json(data)
        except:
            closed.append(ws)

    for ws in closed:
        clients.remove(ws)


@app.websocket("/sync")
async def websocket_endpoint(ws: WebSocket):
    global count
    await ws.accept()
    clients.add(ws)

    # Envoie la valeur actuelle au nouveau client
    await ws.send_json({"value": count})

    try:
        while True:
            msg = await ws.receive_json()
            action = msg.get("action")

            if action == "plus":
                count += 1
            elif action == "minus":
                count -= 1

            await update_all()

    except WebSocketDisconnect:
        clients.remove(ws)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("websocket.main:app", host="127.0.0.1", port=8002, reload=True)
