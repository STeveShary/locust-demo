import json

from flask import Flask, request

from api_demo.alchemy_encoder import AlchemyEncoder
from api_demo.database import db_session
from api_demo.models import Books

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to the mini library!'


@app.route('/books')
def fetch_all():
    return json.dumps(Books.query.all(), cls=AlchemyEncoder)


@app.route('/book')
def fetch_book():
    book_id = request.args.get('id')
    return json.dumps(Books.query.get(book_id), cls=AlchemyEncoder)


# noinspection PyUnusedLocal
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
