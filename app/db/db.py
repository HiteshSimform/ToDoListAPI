# from dotenv import load_dotenv
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from model import task
# from db.base import Base
# from db.sessions import sqlite_engie

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# from model.task import Task
# from db.base import Base


# def create_all_tables():
#     Base.metadata.create_all(bind=sqlite_engie)


from db.sessions import sqlite_engine, postgres_engine
from db.base import Base
from config.config import settings


def get_active_engine():
    return postgres_engine if settings.DATABASE_TYPE == "postgres" else sqlite_engine


def create_all_tables():
    engine = get_active_engine()
    Base.metadata.create_all(bind=engine)
