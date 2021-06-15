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


app = Flask(__name__)


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

    data = SearchBook().do()

    return jsonify(data)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
