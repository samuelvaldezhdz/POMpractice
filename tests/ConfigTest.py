import json
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome


config_path = "config.json"
default_wait = 10
supported_browsers = ["firefox"]


@pytest.fixture(scope="session")
def config():
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def config_browser(config):
    if "browser" not in config:
        raise Exception("The config file does not contain 'browser' ")
    elif config["browser"] not in supported_browsers:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config("browser")


@pytest.fixture(scope="session")
def config_wait_time(config):
    if "wait_time" in config:
        return config["wait_time"]
    else:
        return default_wait


@pytest.fixture(scope="session")
def browser(config_browser, config_wait_time):
    if config_browser == "chrome":
        driver = Chrome()
    elif config_browser == "firefox":
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    driver.implicitly_wait(config_wait_time)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def searchphrase():
    if "search_phrase" not in config:
        raise Exception('The config file does not contain "search_phrase"')
    else:
        return config["search_phrase"]
