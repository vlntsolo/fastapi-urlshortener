import uvicorn
from fastapi import FastAPI
from routes import router
from config import settings
from db.config import engine, Base

app = FastAPI()
app.include_router(router)

if settings.env_name == 'development':
    if __name__ == '__main__':
        uvicorn.run("app:app", port=8001, host='127.0.0.1')

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def hello_world():
    return "PONG"


