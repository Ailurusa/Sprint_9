import allure

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Ожидание загрузки формы входа')
    def wait_login_form(self):
        self.wait_for_visibility(LoginLocators.LOGIN_FORM)

    @allure.step('Ввод email пользователя')
    def set_email(self, email):
        self.fill_field(LoginLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля пользователя')
    def set_password(self, password):
        self.fill_field(LoginLocators.PASSWORD_INPUT, password)

    @allure.step('Отправка формы входа')
    def submit_login(self):
        self.tap(LoginLocators.SUBMIT_BTN)

    @allure.step('Авторизация пользователя')
    def sign_in(self, email, password):
        self.wait_login_form()
        self.set_email(email)
        self.set_password(password)
        self.submit_login()

    @allure.step('Проверка отображения формы авторизации пользователя')
    def check_visibility_login_form(self):
        return self.is_visible(LoginLocators.LOGIN_FORM)

    @allure.step("Получение текущего адреса страницы")
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Проверка отображения формы авторизации пользователя')
    def check_visibility_logout_button(self):
        return self.is_visible(LoginLocators.LOGOUT_LINK)
