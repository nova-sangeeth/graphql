import graphene
import bcrypt
from graphql import GraphQLError

import user_schema
import blog_schema
import crud
import db as database_connection

db_session = database_connection.db_session.session_factory()


class Query(graphene.ObjectType):

    all_blogs = graphene.List(blog_schema.BlogSchema)

    def resolve_all_blogs(self, info):
        query = blog_schema.BlogSchema.get_query(info)  # SQLAlchemy query
        return query.all()

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=False)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: user_schema.UserSchema)

    @staticmethod
    def mutate(root, info, username, email, password, first_name, last_name):
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        user = user_schema.UserSchema(
            username=username,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        ok = True
        db_user = crud.get_user_by_username(db_session, username=username)
        if db_user:
            raise GraphQLError("Username already exists")
        user_info = user_schema.UserCreate(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        crud.create_user(db_session, user_info)
        return CreateUser(user=user, ok=ok)


# class CreateNewBlog(graphene.Mutation):
#     class Arguments:
#         title = graphene.String(required=True)
#         content = graphene.String(required=True)

#         ok = graphene.Boolean()

#         @staticmethod
#         def mutate(self, info, title, content):
#             ok = True


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    # create_new_blog = CreateNewBlog.Field()
