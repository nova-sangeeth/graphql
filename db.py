import os


from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_SQLITE_CONNECTION_STRING = os.getenv("SQLITE_CONN_STRING")
SQLALCHEMY_POSTGRES_CONNECTION_STRING = os.getenv("POSTGRES_CONN_STRING")

# postgres connection string

engine = create_engine(SQLALCHEMY_SQLITE_CONNECTION_STRING)


db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()
