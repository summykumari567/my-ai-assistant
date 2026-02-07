from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
    from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"You said: {req.message}"
    }
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"You said: {req.message}"
    }











