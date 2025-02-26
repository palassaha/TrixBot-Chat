

FROM python:3.10-slim


RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*


RUN curl -L https://ollama.ai/install.sh | sh

WORKDIR /app


RUN pip install --upgrade pip


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--reload"]
