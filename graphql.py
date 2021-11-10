import graphene
import bcrypt
from graphene import String
from graphql import GraphQLError
from starlette.graphql import GraphQLApp


class CreateUser(graphene.Mutation):
    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)
        first_name = String(required=True)
        last_name = String(required=False)
        
    ok = graphene.Boolean()
    user graphene.Field()

        @staticmethod
        def mutate(self, info, username, password, email, first_name, last_name):
            hashed_password = bycrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            ok = True
            return CreateUser(ok=ok)


class AuthenticateUser(graphene.Mutation):
    class Arguments:
        username = String(required=True)
        password = String(required=True)

        ok = graphene.Boolean()

        @staticmethod
        def mutate(self, info, username, password):
            ok = True
            return AuthenticateUser(ok=ok)


class CreateNewBlog(graphene.Mutation):
    class Arguments:
        title = String(required=True)
        content = String(required=True)

        ok = graphene.Boolean()

        @staticmethod
        def mutate(self, info, title, content):
            ok = True
