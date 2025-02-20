
const API_URL = "http://localhost:8000/chat";

async function sendMessage() {
    const input = document.getElementById('user-input');
    const historyDiv = document.getElementById('chat-history');
    
    const userMessage = input.value;
    input.value = '';
    
    // Add user message
    historyDiv.innerHTML += `<div class="user-message">You: ${userMessage}</div>`;
    
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: userMessage,
                history: []
            })
        });
        
        const data = await response.json();
        historyDiv.innerHTML += `<div class="bot-message">Bot: ${data.response}</div>`;
    } catch (error) {
        console.error('Error:', error);
        historyDiv.innerHTML += `<div class="error">Error: Could not get response</div>`;
    }
}