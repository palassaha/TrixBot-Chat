

import requests
from app.config import settings


def generate_response(prompt:str) -> str:
    
    try:
        response = requests.post(
            f"{settings.ollama_endpoint}/api/generate",
            json={
                "model": settings.model_name,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7}
            }
        )
        
        return response.json()["response"]
    
    except Exception as e:
        return f"Error generating response: {str(e)}"