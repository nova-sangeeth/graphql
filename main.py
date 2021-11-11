from fastapi import FastAPI
import graphene
from graphene.types import schema
from starlette.graphql import GraphQLApp
from graphql_mutations import Query, Mutations

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations)))
