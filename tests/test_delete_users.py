import requests

endpoint = '/api/users'


def test_delete_user_success(base_url):
    response = requests.delete(f"{base_url}{endpoint}/2")
    assert response.status_code == 204