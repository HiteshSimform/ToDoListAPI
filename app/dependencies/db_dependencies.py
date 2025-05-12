# from db.sessions import PostgresSessionLocal, SQLiteSessionLocal
# from sqlalchemy.orm import Session
# from typing import Generator


# def get_postgres_session() -> Generator[Session, None, None]:
#     db = PostgresSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# def get_sqlite_session() -> Generator[Session, None, None]:
#     db = SQLiteSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


from db.sessions import PostgresSessionLocal, SQLiteSessionLocal
from sqlalchemy.orm import Session
from typing import Generator
from config.config import settings


def get_db_session() -> Generator[Session, None, None]:
    SessionLocal = (
        PostgresSessionLocal
        if settings.DATABASE_TYPE == "postgres"
        else SQLiteSessionLocal
    )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
