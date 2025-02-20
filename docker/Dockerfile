

FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*


RUN curl -L https://ollama.ai/install.sh | sh

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cachce-dir -r requirements.txt


COPY . . 

RUN ollama pull llama3.2:1b && \
    ollama create trixbot-chat -f ./docker/Modelfile



EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

