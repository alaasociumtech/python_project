import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

books = Table(
    'books',
    metadata,
    Column('book_id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False),
    Column('is_borrowed', Boolean, nullable=False, default=False),
    Column('borrowed_date', DateTime, nullable=True),
    Column('borrowed_by', UUID(as_uuid=True), ForeignKey('members.member_id'), nullable=True),
)

members = Table(
    'members',
    metadata,
    Column('member_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False, unique=True),
)
