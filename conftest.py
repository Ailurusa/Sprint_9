import os
import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from data import make_user
from urls import BASE_URL


@pytest.fixture(scope="function")
def driver():
    selenoid_uri = os.getenv("SELENOID_URI")
    browser_version = os.getenv("BROWSER_VERSION")

    opts = Options()
    opts.add_argument("--window-size=1280,900")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-infobars")

    if browser_version:
        opts.set_capability("browserVersion", browser_version)

    opts.set_capability("unhandledPromptBehavior", "dismiss")

    opts.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False,
        "name": "pytest",
    })

    drv = Remote(command_executor=selenoid_uri, options=opts)
    drv.get(os.getenv("BASE_URL", BASE_URL))
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def user_payload():
    return make_user()
