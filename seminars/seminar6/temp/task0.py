from typing import List
import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine

DATA_URL = 'sqlite:///my_database.db '
database = databases.Database(DATA_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATA_URL)
metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class Item(BaseModel):
    name: str = Field(max_length=10)
    price: float = Field(title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)


class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)


class Order(BaseModel):
    items: List[Item]
    user: User


users = sqlalchemy.Table("users",metadata,sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),sqlalchemy.Column("name", sqlalchemy.String(32)),sqlalchemy.Column("email", sqlalchemy.String(128)),)
engine = create_engine(DATA_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

if __name__ == '__main__':
    uvicorn.run(
        "task0:app",
        host="127.0.0.1",
        port=8000,
        # host="0.0.0.0",
        # port=6000,
        reload=True
    )
