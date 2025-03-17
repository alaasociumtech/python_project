from typing import Any

from sqlalchemy import join, select
from sqlalchemy.engine import Connection

from project.domain.books import Book
from project.infrastructure.database.schema import books, members
from project.infrastructure.repositories.base_repo import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self) -> None:
        super().__init__(Book, books)

    def join_books_and_members(self, connection: Connection) -> Any:

        stmt = (
            select(
                books.c.book_id,
                books.c.title,
                books.c.is_borrowed,
                books.c.borrowed_by,
                members.c.member_id,
                members.c.name.label("member_name")
            )
            .select_from(
                join(books, members, books.c.borrowed_by == members.c.member_id)
            )
        )

        result = connection.execute(stmt)
        return result.fetchall()
