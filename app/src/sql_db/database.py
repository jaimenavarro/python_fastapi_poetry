from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.src import config


SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:admin@{config.SQL_DB_SERVER}/python_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
