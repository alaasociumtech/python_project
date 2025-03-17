from typing import Any
from uuid import UUID

from project.infrastructure.database.schema import books, members
from project.infrastructure.repositories.books_repo import BookRepository
from project.infrastructure.repositories.members_repo import MemberRepository
from project.infrastructure.unit_of_work import UnitOfWork


class BookService:
    def __init__(self) -> None:
        self.book_repo = BookRepository()
        self.member_repo = MemberRepository()

    def get_all_books(self) -> Any:
        with UnitOfWork() as uow:
            return self.book_repo.get_all(uow.connection)

    def get_book_by_id(self, book_id: int) -> Any:
        with UnitOfWork() as uow:
            return self.book_repo.get_by_id(uow.connection, book_id, books.c.book_id)

    def add_book(self, data: dict[str, Any]) -> Any:
        with UnitOfWork() as uow:
            return self.book_repo.add(uow.connection, data)

    def update_book(self, book_id: int, data: dict[str, Any]) -> Any:
        with UnitOfWork() as uow:
            if not (self.book_repo.get_by_id(uow.connection, book_id, books.c.book_id)):
                raise ValueError(f'Book with ID {book_id} not found.')
            self.book_repo.update(uow.connection, book_id, data, books.c.book_id)

    def delete_book(self, book_id: int) -> Any:
        with UnitOfWork() as uow:
            if not (self.book_repo.get_by_id(uow.connection, book_id, books.c.book_id)):
                raise ValueError(f'Book with ID {book_id} not found.')
            self.book_repo.delete(uow.connection, book_id, books.c.book_id)

    def borrow_book(self, book_id: int, member_id: UUID) -> Any:
        with UnitOfWork() as uow:
            if not (book := self.book_repo.get_by_id(uow.connection, book_id, books.c.book_id)):
                raise ValueError(f'Book with ID {book_id} not found.')

            if book.is_borrowed:
                raise ValueError(f'Book with ID {book_id} is already borrowed.')

            if not (self.member_repo.get_by_id(uow.connection, member_id, members.c.member_id)):
                raise ValueError(f'Member with ID {member_id} not found.')

            update_data = {'is_borrowed': True, 'borrowed_by': member_id}
            self.book_repo.update(uow.connection, book_id, update_data, books.c.book_id)

            return self.get_book_by_id(book_id)

    def return_book(self, book_id: int) -> Any:
        with UnitOfWork() as uow:
            if not (book := self.book_repo.get_by_id(uow.connection, book_id, books.c.book_id)):
                raise ValueError(f'Book with ID {book_id} not found.')

            if not book.is_borrowed:
                raise ValueError(f'Book with ID {book_id} is not borrowed.')

            update_data = {'is_borrowed': False, 'borrowed_by': None}
            self.book_repo.update(uow.connection, book_id, update_data, books.c.book_id)

            return self.get_book_by_id(book_id)

    def get_books_with_members(self) -> Any:
        with UnitOfWork() as uow:
            return self.book_repo.join_books_and_members(uow.connection)
