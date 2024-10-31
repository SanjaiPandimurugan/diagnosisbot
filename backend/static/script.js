document.getElementById('diagnostic-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const age = parseInt(document.getElementById('age').value);
    const temperature = parseFloat(document.getElementById('temperature').value);
    const pulse = parseInt(document.getElementById('pulse').value);
    const ecg = parseFloat(document.getElementById('ecg').value);

    // Input validation
    if (age < 0 || age > 120) {
        alert("Please enter a valid age.");
        return;
    }
    if (temperature < 95 || temperature > 105) {
        alert("Please enter a valid temperature.");
        return;
    }
    if (pulse < 30 || pulse > 200) {
        alert("Please enter a valid pulse rate.");
        return;
    }
    if (ecg < 0 || ecg > 2) {
        alert("Please enter a valid ECG value.");
        return;
    }

    // Append user message to chat
    appendMessage(`<i class="fas fa-user"></i> You: Age: ${age}, Temperature: ${temperature}, Pulse: ${pulse}, ECG: ${ecg}`, 'user-message');

    const response = await fetch('/diagnose', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ age, temperature, pulse, ecg })
    });

    const result = await response.json();
    appendMessage(`Bot: ${result.suggestions}`, 'bot-message');
});

// Function to append messages to the chat box
function appendMessage(message, className) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${className}`;
    messageDiv.innerHTML = message; // Use innerHTML to include icons
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}