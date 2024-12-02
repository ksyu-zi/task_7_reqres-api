import requests
from jsonschema import validate
from schemas import post_register_success, post_register_failure
from utils.helpfile import response_logging

endpoint = '/api/register'


def test_register_success(base_url):
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    response_logging(response)
    assert response.status_code == 200
    validate(instance=response.json(), schema=post_register_success)


def test_register_failure(base_url):
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    response_logging(response)
    assert response.status_code == 400
    validate(instance=response.json(), schema=post_register_failure)
