import json
from flask import Flask
from flask_cors import CORS

from client import client

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
basePath = '/api/v1'

@app.route(basePath + '/all')
def all():
    books = client.books.items.find()
    return json.dumps([book for book in books], default=str)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
