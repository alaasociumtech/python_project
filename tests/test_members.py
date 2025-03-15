def test_add_member(client):
    data = {
        'name': 'anas',
        'email': 'anas1@gmail1.com'
    }
    response = client.post('/members', json=data)
    assert response.status_code == 201
    assert 'member_id' in response.get_json()


def test_get_all_members(client):
    response = client.get('/members')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_member_by_id(client):
    data = {
        'name': 'abood',
        'email': 'abood3@gmail1.com'
    }
    post_response = client.post('/members', json=data)
    member_id = post_response.get_json()['member_id']

    response = client.get(f'/members/{member_id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'abood'


def test_update_member(client):
    data = {
        'name': 'Update1',
        'email': 'update4@gmail1.com'
    }
    post_response = client.post('/members', json=data)
    member_id = post_response.get_json()['member_id']

    update_data = {
        'name': 'Updated1',
        'email': 'updated5@gmail1.com'
    }
    response = client.put(f'/members/{member_id}', json=update_data)
    assert response.status_code == 200

    get_response = client.get(f'/members/{member_id}')
    assert get_response.get_json()['name'] == 'Updated1'


def test_delete_member(client):
    data = {
        'name': 'Delete',
        'email': 'delete6@gmial1.com'
    }
    post_response = client.post('/members', json=data)
    member_id = post_response.get_json()['member_id']

    response = client.delete(f'/members/{member_id}')
    assert response.status_code == 200

    second_response = client.delete(f'/members/{member_id}')
    assert second_response.status_code == 404
