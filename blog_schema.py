from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Blog


class BlogBase(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class BlogInformation(BlogBase):
    id: int

    class Config:
        orm_mode = True


class BlogSchema(SQLAlchemyObjectType):
    class Meta:
        model = Blog
        