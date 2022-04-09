from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

DATABASE_URL = settings.db_url
if settings.env_name == "Production":
    DATABASE_URL = settings.db_url.replace('postgres', 'postgresql+asyncpg')

engine = create_async_engine(DATABASE_URL, future=True, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()