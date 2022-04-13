from asyncio.log import logger
from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models import LinkModel
from helpers import generate_slug



class LinkDAL():
    """Shortlink model data access layer"""
    
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_slug(self, url: str):

        #Let check if records exists first
        results = await self.db_session.execute(select(LinkModel).where(LinkModel.url == str(url)))
        old_link = results.scalar_one_or_none()
        if old_link is not None:
            return old_link
        # no existing records -> generating new slug and record
        slug = generate_slug()
        new_link = LinkModel(url=url,slug=slug)
        self.db_session.add(new_link)
        await self.db_session.flush()
        return new_link


    async def get_url(self, slug: str):

        results = await self.db_session.execute(select(LinkModel).where(LinkModel.slug == str(slug)))
        shortlink = results.scalar_one()
        return shortlink