import logging

import pytest
import requests
import time
import logging
import allure
import yaml
def get_test_data():
    with open("testdata/test_data.yaml", "r") as file:
        data = yaml.safe_load(file)
        print(data)
    return [(item["name"], item["email"], item["gender"], item["status"],
             item["expected_code"]) for item in data]

@pytest.mark.parametrize("name, email, gender, status,expected_code", get_test_data())
def test_create_user(name, email, gender, status,expected_code):
    """
    Test to create a new user.
    """
    timestamp = int(time.time())
    email_variable = email.replace("@", str(timestamp)+"@")
    # Create a request object.
    response = requests.post(
        "https://gorest.co.in/public/v2/users",
        headers={"Authorization": "Bearer 046cafd97922a42aad1307f1fd119fbad2083e223b0628060e9a5479f4ef2de8"},
        json={
            "name": name,
            "email": email_variable,
            "gender": gender,
            "status": status
        },
    )
    # Check the status code.
    assert response.status_code == expected_code
    # Check the response body.
    if "name" in response.json():
        assert response.json()["id"] is not None
    else:
        assert str(response.json()["message"]) == "has already been taken"

