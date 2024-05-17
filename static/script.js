async function shortenURL() {
    const longURL = document.getElementById('longURL').value;
    const response = await fetch('/api/shorten', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ longURL })
    });
    const data = await response.json();
    document.getElementById('shortenedURL').value = data.shortURL;
}

function clearContents() {
    document.getElementById('longURL').value = '';
    document.getElementById('shortenedURL').value = '';
}

function redirectToLongURL() {
    const longURL = document.getElementById('longURL').value;
    if (longURL) {
        window.location.href = longURL;
    }
}

function redirectToShortenedURL() {
    const shortenedURL = document.getElementById('shortenedURL').value;
    if (shortenedURL) {
        window.location.href = shortenedURL;
    }
}

function copyShortenedURL() {
    const shortenedURL = document.getElementById('shortenedURL').value;
    navigator.clipboard.writeText(shortenedURL).then(function() {
        alert('Shortened URL copied to clipboard!');
    }, function() {
        alert('Failed to copy shortened URL to clipboard.');
    });
}
