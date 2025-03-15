from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from project.domain.base_entity import BaseEntity


@dataclass
class Book(BaseEntity):
    book_id: int
    title: str
    author: int
    is_borrowed: bool = False
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[int] = None
