import os
import asyncio

from flask import (
    Flask,
    g,
    jsonify,
    request
)
from flask_cors import CORS

from .application.exceptions import WrongDataException
from .application import (
    CreateBook,
    SearchBook
)
from .infrastructure.controllers.exceptions import BadRequestException
from .infrastructure.controllers.utils import DecimalEncoder

app = Flask(__name__)
CORS(app)
app.json_encoder = DecimalEncoder


@app.errorhandler(BadRequestException)
@app.errorhandler(WrongDataException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response


@app.route('/api/v1/book', methods=['POST', 'GET'])
def books():
    if request.method == 'GET':
        data = asyncio.run(SearchBook().do(**request.args))
        return jsonify(data)

    book = asyncio.run(CreateBook().do(**request.json))
    return jsonify(book)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
