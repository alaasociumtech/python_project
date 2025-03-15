from project.domain.books import Book
from project.infrastructure.database.schema import books
from project.infrastructure.repositories.base_repo import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self) -> None:
        super().__init__(Book, books)
