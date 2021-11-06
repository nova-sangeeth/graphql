from pydantic import BaseModel
from models import User, Blog
from graphene_sqlalchemy import SQLAlchemyObjectType


class UserBase:
    username: str


class UserCreate(UserBase):
    email: str
    first_name: str
    last_name: str
    password: str


class UserAuth(UserBase):
    password: str


class UserInformation(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = User