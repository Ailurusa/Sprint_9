import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data import make_user


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())  # скачает совместимый драйвер под Chrome 139
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_payload():
    return make_user()



