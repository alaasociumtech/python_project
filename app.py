from flask import Flask
from project.presentation.books_view import BookAPI, BooksWithMembersAPI, BorrowAPI, ReturnAPI
from project.presentation.members_view import MemberAPI


def create_app():
    app = Flask(__name__)

    book_view = BookAPI.as_view('book_api')
    app.add_url_rule('/books', defaults={'book_id': None}, view_func=book_view, methods=['GET'])
    app.add_url_rule('/books', view_func=book_view, methods=['POST'])
    app.add_url_rule('/books/<int:book_id>', view_func=book_view, methods=['GET', 'PATCH', 'DELETE'])

    borrow_view = BorrowAPI.as_view('borrow_api')
    app.add_url_rule('/borrow/<int:book_id>/<uuid:member_id>', view_func=borrow_view, methods=['POST'])

    return_view = ReturnAPI.as_view('return_api')
    app.add_url_rule('/return/<int:book_id>', view_func=return_view, methods=['POST'])

    member_view = MemberAPI.as_view('member_api')
    app.add_url_rule('/members', defaults={'member_id': None}, view_func=member_view, methods=['GET'])
    app.add_url_rule('/members', view_func=member_view, methods=['POST'])
    app.add_url_rule('/members/<uuid:member_id>', view_func=member_view, methods=['GET', 'PATCH', 'DELETE'])

    books_with_members_view = BooksWithMembersAPI.as_view('books_with_members_api')
    app.add_url_rule('/books-with-members', view_func=books_with_members_view, methods=['GET'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
