from typing import Any
from uuid import UUID

from flask import jsonify, request
from flask.views import MethodView

from project.application.books_service import BookService

book_service = BookService()


class BookAPI(MethodView):

    def get(self, book_id: int | None = None) -> Any:
        if book_id is None:
            books = book_service.get_all_books()
            return jsonify([vars(book) for book in books])
        else:
            book = book_service.get_book_by_id(book_id)
            if not book:
                return jsonify({'message': 'Book not found'}), 404
            return jsonify(book.__dict__)

    def post(self) -> Any:
        data: dict[str, Any] | None = request.json
        if data is None:
            return jsonify({'message': 'Invalid JSON payload'}), 400
        book_id = book_service.add_book(data)
        return jsonify({'message': 'Book added', 'book_id': book_id}), 201

    def patch(self, book_id: int) -> Any:
        data: dict[str, Any] | None = request.json
        if data is None:
            return jsonify({'message': 'Invalid JSON payload'}), 400
        try:
            book_service.update_book(book_id, data)
            return jsonify({'message': 'Book updated'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 404

    def delete(self, book_id: int) -> Any:
        try:
            book_service.delete_book(book_id)
            return jsonify({'message': 'Book deleted'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 404


class BorrowAPI(MethodView):

    def post(self, book_id: int, member_id: UUID) -> Any:
        try:
            borrowed_book = book_service.borrow_book(book_id, member_id)
            return jsonify(borrowed_book.__dict__)
        except ValueError as e:
            return jsonify({'message': str(e)}), 400


class ReturnAPI(MethodView):

    def post(self, book_id: int) -> Any:
        try:
            returned_book = book_service.return_book(book_id)
            return jsonify(returned_book.__dict__)
        except ValueError as e:
            return jsonify({'message': str(e)}), 400


class BooksWithMembersAPI(MethodView):
    def get(self) -> Any:
        books_with_members = book_service.get_books_with_members()
        return jsonify([dict(row._mapping) for row in books_with_members])
