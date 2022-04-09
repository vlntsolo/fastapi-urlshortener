from sqlalchemy import Column, String, DateTime, func #Integer
from sqlalchemy.orm import  declarative_mixin #sessionmaker, relationship, backref,
from db.config import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


@declarative_mixin
class IDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

@declarative_mixin
class CreatedAtMixin:
    """Mixin for record creation timestamps."""
    created_at = Column(DateTime(), default=func.now())


class LinkModel(Base, IDMixin, CreatedAtMixin):
    __tablename__ = 'shortlinks'

    url = Column(String, nullable=False)
    slug = Column(String, nullable=False)



# class Book(Base):
#     __tablename__ = 'books'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     author = Column(String, nullable=False)
#     release_year = Column(Integer, nullable=False)