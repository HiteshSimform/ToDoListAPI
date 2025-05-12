from fastapi import FastAPI
from db.db import create_all_tables
from model import task
from db.base import Base
from contextlib import asynccontextmanager
# from routers import task_router
from routers import task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/a")
def read_root():
    return {"message": "Welcome to your FastAPI project!"}

app.include_router(task_router.router)