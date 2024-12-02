import requests
from utils.helpfile import response_logging

endpoint = '/api/users'


def test_post_user_success(base_url):
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    response_logging(response)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"