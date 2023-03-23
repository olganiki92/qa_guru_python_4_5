import pytest
from selene import browser


@pytest.fixture()
def config_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    return browser
