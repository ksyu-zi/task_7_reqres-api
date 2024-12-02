import requests
from jsonschema import validate
from schemas import post_login_success, post_login_failure
from utils.helpfile import response_logging

endpoint = '/api/login'


def test_login_success(base_url):
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    response_logging(response)
    assert response.status_code == 200
    validate(instance=response.json(), schema=post_login_success)


def test_login_failure(base_url):
    payload = {"email": "peter@klaven"}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    response_logging(response)
    assert response.status_code == 400
    validate(instance=response.json(), schema=post_login_failure)
