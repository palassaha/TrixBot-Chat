

import pytest
import requests

BASE_URL = "http://localhost:8000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_chat_endpoint():
    payload = {
        "content": "What are the main events?",
        "history": []
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()