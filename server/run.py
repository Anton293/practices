from flask import Flask
from flask_cors import CORS
from flask import request, jsonify, render_template
import requests


app = Flask(__name__)
CORS(app)


@app.route('/search')
def search():
    text = request.args.get('text')
    result = requests.get(f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDzAyK8U9wLso-zX-SCs6zJGzDNzCK3Lao&cx=21d680efd33df4831&q={text}')
    return result.json()


if __name__ == '__main__':
    app.run(debug=True, port=5000)