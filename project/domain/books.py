from dataclasses import dataclass
from datetime import datetime

from project.domain.base_entity import BaseEntity


@dataclass
class Book(BaseEntity):
    book_id: int
    title: str
    author: int
    is_borrowed: bool = False
    borrowed_date: datetime | None = None
    borrowed_by: int | None = None
