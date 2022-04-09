from pydantic import BaseModel, UUID4, HttpUrl


class BaseID(BaseModel):
    id: UUID4


class LinkRequestSchema(BaseModel):
    url: HttpUrl