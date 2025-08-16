import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ждем, пока элемент станет видимым')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Клик по элементу')
    def tap(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Ввод текста в поле')
    def fill_field(self, locator, text):
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(text)

    @allure.step('Получение текста элемента')
    def extract_text(self, locator):
        return self.browser.find_element(*locator).text

    @allure.step('Проверка, что элемент отображается')
    def is_visible(self, locator):
        try:
            return self.browser.find_element(*locator).is_displayed()
        except Exception:
            return False

    @allure.step('Поиск одного элемента')
    def get_element(self, locator):
        method, value = locator
        return self.browser.find_element(method, value)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.browser.current_url

    @allure.step("Открываем URL")
    def open_url(self, url: str, page_ready_timeout: int = 10):
        self.browser.get(url)
        WebDriverWait(self.browser, page_ready_timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Ждем URL")
    def wait_url_is(self, url: str, timeout: int = 15):
        WebDriverWait(self.browser, timeout).until(EC.url_to_be(url))
