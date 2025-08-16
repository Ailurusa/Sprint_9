import allure

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from urls import RECIPES_URL


class TestLogin:
    @allure.title("Успешная авторизация переносит на главную и показывает «Выход»")
    def test_success_login_redirects_and_logout_visible(self, driver, user_payload):
        reg = RegistrationPage(driver)
        reg.register(
            user_payload.first_name,
            user_payload.last_name,
            user_payload.username,
            user_payload.email,
            user_payload.password
        )
        login = LoginPage(driver)
        login.sign_in(user_payload.email, user_payload.password)
        current_url = login.get_current_page_url()
        assert current_url == RECIPES_URL and login.check_visibility_logout_button()
