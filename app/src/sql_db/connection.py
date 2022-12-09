from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.src.config import config

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{config.SQL_DB_USER}:{config.SQL_DB_PASSWORD}@{config.SQL_DB_SERVER}/{config.SQL_DB_SCHEMA}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()