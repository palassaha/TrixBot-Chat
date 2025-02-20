

from app.config import settings

def format_prompt(query: str, history: list) -> str:
    system_msg = "You are Trix Bot - TechTrix 2025 assistant. Provide accurate information about events."
    history_str = "\n".join(
        [f"User: {h['user']}\nAssistant: {h['assistant']}" 
        for h in history[-settings.max_history_length:]]
    )
    
    return f"""
    {system_msg}
    
    Context:
    {history_str}
    
    Question: {query}
    
    Answer:"""