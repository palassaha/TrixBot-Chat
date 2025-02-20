

FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://ollama.ai/install.sh | sh

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir r requirements.txt

COPY . .

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 7860

CMD ["/start.sh"]

