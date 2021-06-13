import os

from flask import (
    Flask,
    g,
    jsonify,
    request
)

from src.application import WrongDataException
from src.application import (
    CreateBook,
    SearchBook
)
from infrastructure.controllers.exceptions import BadRequestException
from infrastructure.controllers.utils import utility
from src.infrastructure.database import (
    close_db_connection,
    init_db_engine,
    db_connect
)
from src.infrastructure.repositories import BookRepository


app = Flask(__name__)


def get_db_connection(app):
    if 'db_con' not in g:
        db_engine = app.config.get('DB_ENGINE', None) or init_db_engine()
        g.db_con = db_connect(db_engine)
    return g.db_con


@app.errorhandler(BadRequestException)
@app.errorhandler(WrongDataException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response


@app.route('/book/create', methods=['POST'])
def create():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})

    plain_text = CreateBook().do()

    return jsonify({'plain_text': plain_text})


@app.route('/book', methods=['GET'])
def search():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})

    data = SearchBook().do(
        payload='',
        repository=BookRepository(get_db_connection(app))
    )

    return jsonify(data)


@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
