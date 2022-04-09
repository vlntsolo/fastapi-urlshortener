from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, Header
from db.schemas import (
    LinkRequestSchema, 
)
from db.dals import LinkDAL
from typing import Optional
from dependencies import get_link_dal
from helpers import format_short_url

router = APIRouter()

@router.post('/api/new')
async def create_short(item: LinkRequestSchema, Authorization: Optional[str] = Header(None), link_dal: LinkDAL = Depends(get_link_dal)):
    print("Authorization", Authorization)
    data = await link_dal.create_slug(item.url)
    short_url = format_short_url(data.slug)
    return {"short": short_url}


@router.get('/{slug}')
async def proccess_redirect(slug: str, link_dal: LinkDAL = Depends(get_link_dal)):
    data = await link_dal.get_url(slug)
    return RedirectResponse(url=data.url)
