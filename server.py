from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for all routes

# Add security headers for SharedArrayBuffer support (required for SPZ functionality)
@app.after_request
def add_security_headers(response):
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

# Serve the main HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'test-spz-positioning.html')

# Serve static files (CSS, JS, images)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)