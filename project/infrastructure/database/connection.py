from sqlalchemy import create_engine

DATABASE_URL = 'postgresql://postgres:mysecretpassword@localhost:5432/books'

engine = create_engine(DATABASE_URL)
