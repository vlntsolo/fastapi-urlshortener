import uvicorn
from fastapi import FastAPI
from db.config import engine, Base, async_session
from db.dals import BookDAL
from db.models import Book
from typing import List, Optional
from routes import router

app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("app:app", port=8001, host='127.0.0.1')

# @app.on_event("startup")
# async def startup():
#     # create db tables
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def hello_world():
    return "hello_world"
