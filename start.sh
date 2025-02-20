

ollama serve & 
sleep 5

ollama pull llama3:2:1b
ollama create trixbot-chat -f ./docker/Modelfile

uvicorn app.main:app --host 0.0.0.0 --port 8000
