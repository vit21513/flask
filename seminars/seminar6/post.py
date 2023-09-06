from sqlalchemy import select
from sqlalchemy.sql.functions import user

from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get('/posts/', response_model=dict)
async def get_post():
    return {"message": "ok"}


@router.post('/posts/', response_model=dict)
async def inp_post(post: InputPost):
    queue = post_db.insert().values(
        user_id=post.us_id,
        post=post.post, )
    last = await  db.execute(queue)
    return {**post.dict(), 'id': last}


@router.post('/post_all/', response_model=list[Post])
async def get_post():

    query = sqlalchemy.select(
    post_db.c.id, post_db.c.post,
    users_db.c.id.label("user_id"),
    users_db.c.login).join(users_db)
    rows = await db.fetch_all(query)
    res =[]
    # for row in rows:
    #     res.append(Post(id=row.id,
    #                     post=row.post,
    #                     user=User(
    #                         id=row.user_id,
    #                         login=row.login,
    #                         password="1234567",
    #                         email="vff@fff.tt")))
    # return [res for r in rows]
    return [Post(id=row.id, post=row.post, user=User(id=row.user_id, login=row.login, password='xxxxxx', email='zzzzzz')) for row in rows]

