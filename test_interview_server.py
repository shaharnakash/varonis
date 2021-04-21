import requests
import pytest


@pytest.mark.api_server
def test_api_server_auth_fail() -> None:
    base_url = "http://0.0.0.0:8000/"
    response = requests.get("{}api/auth".format(base_url))
    assert response.status_code == 500

@pytest.mark.api_server
def test_api_server() -> None:
    base_url = "http://0.0.0.0:8000/"
    base_api = "http://0.0.0.0:8000/api/poly/"
    # auth
    response = requests.post("{}api/auth".format(base_url), json={"username": "test", "password": "1234"},
                             headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    response_content = response.json()
    access_token = response_content.get("access_token")

    # post object and fetch id
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer {}".format(access_token)}
    response = requests.post(base_api,
                             json={"data": [{"key": "key1", "val": "val1", "valType": "str"}]},
                             headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    response_content = response.json()
    object_id = response_content.get("id")

    # get all objects and search for object id from post
    response = requests.get(base_api, headers=header)
    assert response.status_code == 200
    response_body = response.json()
    print(response_body)

    # get object by id
    response = requests.get(base_api+str(object_id), headers=header)
    assert response.status_code == 200
    response_body = response.json()
    print(response_body)

    #delete object by id
    response = requests.delete(base_api+str(object_id), headers=header)
    assert response.status_code == 200
    response_body = response.json()
    print(response_body)
    # assert object_id not in response_content.get("id")

    response = requests.get(base_api, headers=header)
    assert response.status_code == 200
    response_body = response.json()
    print(response_body)
    assert [] == (list(filter(lambda x: x["object_id"] == object_id, response_body)))
