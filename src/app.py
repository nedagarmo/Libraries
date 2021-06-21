import os
import graphene

from flask import Flask, jsonify
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_graphql_auth import GraphQLAuth

from .infrastructure.mutations import MainMutation
from .infrastructure.queries import BookQuery
from .application.exceptions import WrongDataException
from .infrastructure.controllers.exceptions import BadRequestException
from .infrastructure.controllers.utils import DecimalEncoder

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "3c3adab4978467a956a8265ba178e1f95810a320d09c9f6dac8ae2423a316869"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 10
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 30
auth = GraphQLAuth(app)
app.json_encoder = DecimalEncoder


@app.errorhandler(BadRequestException)
@app.errorhandler(WrongDataException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response


schema = graphene.Schema(query=BookQuery, mutation=MainMutation)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql', schema=schema, graphiql=True
))


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
