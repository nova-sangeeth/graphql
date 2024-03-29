from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %r>" % (self.username)


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))
