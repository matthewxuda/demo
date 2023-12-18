import pytest
import requests
import time

def test_get_users():
    """
    Test to get the list of users.
    """

    # Create a request object.
    request = requests.get(
        "https://gorest.co.in/public/v2/users",
        headers={"Authorization": "Bearer 046cafd97922a42aad1307f1fd119fbad2083e223b0628060e9a5479f4ef2de8"},
    )

    # Check the status code.
    assert request.status_code == 200

    # Check the response body.

