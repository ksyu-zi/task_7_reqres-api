import requests
from jsonschema import validate
from schemas import get_users, get_user

endpoint = '/api/users'


def test_get_users(base_url):
    response = requests.get(f"{base_url}{endpoint}", params={"page": 2})
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_users)


def test_get_user_by_id(base_url):
    response = requests.get(f"{base_url}{endpoint}/2")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_user)


def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}{endpoint}/23")
    assert response.status_code == 404
    assert response.json() == {}