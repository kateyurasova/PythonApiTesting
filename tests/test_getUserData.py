import requests
import allure

BASE_URL = "https://reqres.in"

class TestGetUserData(object):
    @allure.feature('Saving of users data')
    @allure.story('Get list of users')
    def test_one(self):
        response = requests.get(BASE_URL + "/api/users?page=2")
        userData = response.json()

        assert response.status_code == 200, 'Response code in wrong'
        assert userData['per_page'] == 3, 'Page value is not equal to the expected value'

    @allure.feature('Saving of users data')
    @allure.story('Get single user data')
    def test_two(self):
        response = requests.get(BASE_URL + "/api/users/2")
        userData = response.json()['data']
        assert response.status_code == 200
        assert userData['first_name'] == "Janet"
        assert userData['last_name'] == "Weaver"
        assert userData['avatar'] == "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
