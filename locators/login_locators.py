from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Войти']")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Выход']")
    LOGIN_FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz.styles_form__2_42b")
