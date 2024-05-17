import hashlib
from flask import redirect 

url_database = {}

def shorten_url(long_url):
    # Generate SHA-256 hash of the long URL
    hash_object = hashlib.sha256(long_url.encode())
    short_code = hash_object.hexdigest()[:8]  # Take the first 8 characters of the hash as the short code
    url_database[short_code] = long_url
    return f'http://localhost:5000/{short_code}'

def redirect_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return 'URL not found', 404
