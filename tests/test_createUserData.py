import requests
import allure
import pytest
import logging

from strgen import StringGenerator

BASE_URL = "https://reqres.in"

logger = logging.getLogger('foo')


@pytest.mark.parametrize("name,job", [
    (StringGenerator('[\l\d]{1:1}').render(), StringGenerator('[\l\d]{1:1}').render()),
    (StringGenerator('[\l\d]{20:20}').render(), StringGenerator('[\l\d]{20:20}').render()),
    (StringGenerator('[\d]{4:20}').render(), StringGenerator('[\d]{4:20}').render())],
                         ids=["Values with min length",
                              "Values with max length",
                              "Random numeric values"])
class TestCreateUserData(object):
    @allure.feature('User is able to create user in the system')
    @allure.story('Create User:')
    def test_create_user(self, name, job):
        # Testing data
        user_data = {
            "name": "%s" % name,
            "job": "%s" % job
        }
        logger.info("Testing data is prepared...")
        logger.info("CREATE USER WITH DATA")
        logger.info(user_data)

        logger.info("WHEN performing API call")
        response = requests.post(BASE_URL + "/api/users", user_data)

        logger.info("THEN Verify that response code is equal to 201")
        assert response.status_code == 201, 'Response code in wrong'
        logger.info("AND Verify that name in response is equal to %s" % user_data['name'])
        assert response.json()['name'] == user_data['name']
        logger.info("AND Verify that job in response is equal to %s" % user_data['job'])
        assert response.json()['job'] == user_data['job']
