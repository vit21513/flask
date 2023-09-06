import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.responses import HTMLResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.get("/")
# async def root():
#     return {"message": "Hellyyyo World"}


"""pip install 'uvicorn[standart]   установить сервер
uvicorn app.app --reload
если путь то через точку seminars.seminars4.lecia.app:app --reload
"""

""""http://127.0.0.1:8000/item_id/10?q=fhgdgdf"""


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.get("/item_id/{item_id}")
async def read(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}




@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


