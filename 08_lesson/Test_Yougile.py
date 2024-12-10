import requests

token = 'QlHtq-S8ql4h8QE6HWFKayh9oDyLw8HNIpcv5MJ0Y6jE8DStqvqgmMlNNUKm-d7G'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def test_get_projects():
    url = 'https://ru.yougile.com/api-v2/projects'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'content' in response.json()

def test_create_projects():
    url = 'https://ru.yougile.com/api-v2/projects'
    body = {"title": "Домашнее задание №8"}
    response = requests.post(url, headers=headers,json=body)

    assert response.status_code == 201
    assert 'id' in response.json()

def test_modify_projects():
    url = 'https://ru.yougile.com/api-v2/projects'
    body = {"title": "Домашнее задание №8"}
    response = requests.post(url, headers=headers, json=body)
    id=response.json()["id"]
    url = f'https://ru.yougile.com/api-v2/projects/{id}'
    body = {"title": "Обновленное название"}
    response = requests.put(url, headers=headers, json=body)

    assert response.status_code == 200
    assert 'id' in response.json()

def test_get_project_by_id():
    url = 'https://ru.yougile.com/api-v2/projects'
    body = {"title": "Домашнее задание №8"}
    response = requests.post(url, headers=headers, json=body)
    id = response.json()["id"]
    url = f'https://ru.yougile.com/api-v2/projects/{id}'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'id' in response.json()

def test_get_projects_negative():
    url = 'https://ru.yougile.com/api-v2/projects'
    response = requests.get(url)

    assert response.status_code == 401

def test_create_projects_negative():
    url = 'https://ru.yougile.com/api-v2/projects'
    body = {}
    response = requests.post(url, headers=headers,json=body)

    assert response.status_code == 400

def test_create_projects_negative_2():
    url = 'https://ru.yougile.com/api-v2/projects'
    body = {"title":""}
    response = requests.post(url, headers=headers, json=body)

    assert response.status_code == 400
