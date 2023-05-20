from typing import List
from uuid import uuid4

from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="sameer",
        last_name="shaikh",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="alexa",
        last_name="jones",
        gender=Gender.female,
        roles=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/users")
async def get_users():
    return db
