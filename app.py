from flask import Flask
from client import client

app = Flask(__name__)
basePath = '/api/v1'

@app.route(basePath + '/all')
def all():
    books = client.books.items.find()
    return str(list(books))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
