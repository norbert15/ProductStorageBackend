from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL = 'mysql+mysqlconnector://root:@localhost:3306/webshop'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base()