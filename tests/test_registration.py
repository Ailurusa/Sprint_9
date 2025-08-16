import allure

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from urls import LOGIN_URL


class TestRegistration:
    @allure.title("Регистрация пользователя")
    def test_registration(self, driver, user_payload):
        reg = RegistrationPage(driver)
        reg.register(
            user_payload.first_name,
            user_payload.last_name,
            user_payload.username,
            user_payload.email,
            user_payload.password
        )
        current_url = reg.get_current_page_url()
        login_page = LoginPage(driver)
        check_login = login_page.check_visibility_login_form()
        assert current_url == LOGIN_URL and check_login
