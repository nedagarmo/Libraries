import graphene
from flask_graphql_auth import create_access_token, create_refresh_token, mutation_jwt_refresh_token_required, \
    get_jwt_identity


class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, password):
        # TODO: Esto podría reemplazarse por una llamada a base de datos para verificar si el usuario se encuentra
        #  registrado.
        user = username == password
        if not user:
            raise Exception('Error de autenticación: Usuario no registrado')
        return AuthMutation(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username)
        )


class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self, _):
        current_user = get_jwt_identity()
        return RefreshMutation(
            new_token=create_access_token(identity=current_user),
        )
