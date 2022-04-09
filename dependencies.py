from db.config import async_session
from db.dals import LinkDAL


async def get_link_dal():
    async with async_session() as session:
        async with session.begin():
            yield LinkDAL(session)