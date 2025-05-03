function analyzeText() {
    const text = document.getElementById('text-input').value;
    fetch('/analyze-text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, lang: 'en' })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h3>Classification: ${data.classification}</h3>
            <p>Reason: ${data.reason}</p>
        `;
    });
}

function checkUrl() {
    const url = document.getElementById('url-input').value;
    fetch('/check-url', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h3>URL Safety: ${data.safe ? 'Safe' : 'Unsafe'}</h3>
        `;
    });
}

function analyzeAudio() {
    const fileInput = document.getElementById('audio-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/analyze-audio', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h3>Classification: ${data.classification}</h3>
            <p>Reason: ${data.reason}</p>
        `;
    });
}
