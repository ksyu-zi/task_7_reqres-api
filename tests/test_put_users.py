import requests
from jsonschema import validate
from schemas import put_users

endpoint = '/api/users'


def test_put_update_users(base_url):
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(f"{base_url}{endpoint}/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    validate(instance=response.json(), schema=put_users)
