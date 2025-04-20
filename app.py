from flask import Flask
from client import client

app = Flask(__name__)

@app.route('/')
def all():
    books = client.books.items.find()
    return str(list(books))

if __name__ == '__main__':
    app.run(debug=True)
