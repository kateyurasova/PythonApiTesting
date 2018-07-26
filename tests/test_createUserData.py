import requests
import allure
import pytest
import logging

from strgen import StringGenerator

BASE_URL = "https://reqres.in"


logger = logging.getLogger('foo')

@pytest.mark.parametrize("description,first_name, last_name", [
    ("min length values", StringGenerator('[\l\d]{1:1}').render(), StringGenerator('[\l\d]{1:1}').render()),
    ("max length values", StringGenerator('[\l\d]{20:20}').render(), StringGenerator('[\l\d]{20:20}').render()),
    ("random numeric values", StringGenerator('[\d]{4:20}').render(), StringGenerator('[\d]{4:20}').render()),
])

class TestCreateUserData(object):
    @allure.feature('Create user data')
    @allure.story('Create User')
    def test_one(self, description, first_name, last_name):
        # Testing data
        user_data = {
            "name": "%s" % first_name,
            "job": "%s" % last_name
        }
        logger.info("Testing data is prepared...")
        logger.info("CREATE USER WITH DATA")
        logger.info(user_data)

        response = requests.post(BASE_URL + "/api/users", user_data)

        assert response.status_code == 201, 'Response code in wrong'
        assert response.json()['name'] == user_data['name']
        assert response.json()['job'] == user_data['job']
