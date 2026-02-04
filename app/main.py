#Uvicorn: É o servidor que escuta as requisições da internet e as repassa para o FastAPI.  

from fastapi import FastAPI

app = FastAPI(title="Chatbot Backend")

@app.get("/health")
def health():
    return {"status": "online"}