

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.utils import model_handler, prompt_formatter
from app.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str
    history : list = []
    

@app.get("/")
def read_root():
    return {"message": "Hi This is Trix-Bot the officaial assistant of TechTrix 2025"}

@app.post("/chat")
async def chat(message: Message):
    try:
        prompt = prompt_formatter.format_prompt(
            message.content,
            message.history   
        )
        
        response = model_handler.generate_response(prompt)
        return {"response": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/health")
def health_check():
    return {"status": "healthy"}