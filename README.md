Project Name: Library Management System

Description:
A RESTful API to manage a library system.
Functions:

Manage books and members.
Borrow and return books.
CRUD operations for both entities.

Setup Instructions:

1. Clone the Repository
   git clone <repository-url>
   cd project/

2. Create a Virtual Environment
   pyenv virtualenv 3.10.4 pyenv_name
   pyenv activate pyenv_name

3. Install Dependencies
   pip install -r requirements.txt

4. Database Setup
   Make sure PostgreSQL is running.
   Create a database
   Update the database connection string in infrastructure/database/connection.py

Running the Application:
python app.py

API Endpoints:

Books:
POST /books — Add a new book.
GET /books — Get a list of all books.
GET /books/<book_id> — Get a book by its ID.
PUT /books/<book_id> — Update a book's details.
DELETE /books/<book_id> — Delete a book.

Members:
POST /members — Add a new member.
GET /members — Get all members.
GET /members/<member_id> — Get a member by their ID.
PUT /members/<member_id> — Update a member's information.
DELETE /members/<member_id> — Delete a member.

Borrowing and Returning Books:
POST /borrow/<book_id>/<member_id> — Borrow a book.
POST /return/<book_id> — Return a borrowed book.
