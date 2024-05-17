from flask import Flask, request, redirect, jsonify, render_template
from controllers.url_controller import shorten_url, redirect_url

app = Flask(__name__)

@app.route('/api/shorten', methods=['POST'])
def shorten():
    long_url = request.json.get('longURL')
    if long_url:
        shortened_url = shorten_url(long_url)
        return jsonify({'shortURL': shortened_url}), 200
    else:
        return jsonify({'error': 'Missing longURL parameter'}), 400

@app.route('/<short_code>')
def redirect_short_url(short_code):
    return redirect_url(short_code)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
