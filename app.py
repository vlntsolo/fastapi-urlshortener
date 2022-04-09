import uvicorn
from fastapi import FastAPI
from routes import router
from config import settings
from db.config import engine, Base

app = FastAPI()
app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     # create db tables
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def hello_world():
    return "PONG"


