def test_add_book(client):
    data = {
        'title': 'Book1',
        'author': 'Author1'
    }
    response = client.post('/books', json=data)
    assert response.status_code == 201
    assert 'book_id' in response.get_json()


def test_get_all_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_borrow_and_return_book(client):
    member_data = {
        'name': 'Borrow',
        'email': 'borrow@any1.com'
    }
    member_response = client.post('/members', json=member_data)
    member_id = member_response.get_json()['member_id']

    book_data = {
        'title': 'Borrowed',
        'author': 'Author1'
    }
    book_response = client.post('/books', json=book_data)
    book_id = book_response.get_json()['book_id']

    borrow_response = client.post(f'/borrow/{book_id}/{member_id}')
    assert borrow_response.status_code == 200

    second_borrow = client.post(f'/borrow/{book_id}/{member_id}')
    assert second_borrow.status_code == 400

    return_response = client.post(f'/return/{book_id}', json={'member_id': member_id})
    assert return_response.status_code == 200

    second_return = client.post(f'/return/{book_id}', json={'member_id': member_id})
    assert second_return.status_code == 400


def test_delete_book(client):
    book_data = {
        'title': 'Book',
        'author': 'Author'
    }
    book_response = client.post('/books', json=book_data)
    book_id = book_response.get_json()['book_id']

    delete_response = client.delete(f'/books/{book_id}')
    assert delete_response.status_code == 200

    second_delete = client.delete(f'/books/{book_id}')
    assert second_delete.status_code == 404
