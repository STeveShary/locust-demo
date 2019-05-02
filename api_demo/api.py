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
def fetch_multiple():
    book_ids = request.args.get('ids').split(",")
    return json.dumps(Books.query.filter(Books.id.in_(book_ids)).all(), cls=AlchemyEncoder)


@app.route('/book-title')
def fetch_by_title():
    title = request.args.get('title')
    return json.dumps(Books.query.filter(Books.title.like(f"%{title}%")).all(), cls=AlchemyEncoder)


@app.route('/book')
def fetch_book():
    book_id = request.args.get('id')
    return json.dumps(Books.query.get(book_id), cls=AlchemyEncoder)


# noinspection PyUnusedLocal
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
