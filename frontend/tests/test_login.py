from pytest import fixture
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def test_login(driver, base_url):
    driver.get(base_url)
    assert "Shoppe" in driver.title
    assert 1 == 1
