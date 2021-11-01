import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQLALCHEMY_POSTGRES_CONNECTION_STRING = os.getenv("POSTGRES_CONN_STRING")

# postgres connection string
engine = create_engine(SQLALCHEMY_POSTGRES_CONNECTION_STRING)


db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()
