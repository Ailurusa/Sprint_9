import allure

from locators.registration_locators import RegistrationLocators
from pages.base_page import BasePage
from urls import REGISTER_URL, LOGIN_URL


class RegistrationPage(BasePage):
    @allure.step('Ожидание загрузки формы входа')
    def wait_registration_form(self):
        self.wait_for_visibility(RegistrationLocators.REGISTER_FORM)

    @allure.step('Ввод имени пользователя')
    def set_first_name(self, first_name):
        self.fill_field(RegistrationLocators.FIRST_NAME_INPUT, first_name)

    @allure.step('Ввод фамилии пользователя')
    def set_last_name(self, last_name):
        self.fill_field(RegistrationLocators.LAST_NAME_INPUT, last_name)

    @allure.step('Ввод логина пользователя')
    def set_username(self, username):
        self.fill_field(RegistrationLocators.USERNAME_INPUT, username)

    @allure.step('Ввод email пользователя')
    def set_email(self, email):
        self.fill_field(RegistrationLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля пользователя')
    def set_password(self, password):
        self.fill_field(RegistrationLocators.PASSWORD_INPUT, password)

    @allure.step('Отправка формы входа')
    def submit_registration(self):
        self.tap(RegistrationLocators.REGISTER_SUBMIT_BUTTON)

    @allure.step('Регистрация пользователя')
    def register(self, first_name, last_name, username, email, password):
        self.open()
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)
        self.submit_registration()
        self.wait_opened()

    @allure.step("Получение текущего адреса страницы")
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Открываем страницу регистрации')
    def open(self):
        self.open_url(REGISTER_URL)
        self.wait_registration_form()

    @allure.step("Ожидать, что страница авторизации открыта")
    def wait_opened(self):
        self.wait_url_is(LOGIN_URL)
