from pytest import fixture
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By



@fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


def test_my_profile_redirect(driver, base_url):
    driver.get(base_url)
    driver.implicitly_wait(3)
    assert "Shoppe" in driver.title
    my_profile = driver.find_element(By.CSS_SELECTOR, "[href='/my-profile']")
    my_profile.click()
    assert driver.current_url.endswith("/login")


def test_login_email(driver, base_url):
    driver.get(base_url+"/login")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    email_form = driver.find_element(By.ID, "mat-input-1")
    email_form.send_keys("wr@sdfsd")
    assert submit_button.is_enabled() is False
    email_form.send_keys("124.@dfgf.fg")
    assert submit_button.is_enabled() is False
    email_form.send_keys("bob.mrley@example")
    assert submit_button.is_enabled() is False
    email_form.send_keys("@example.com")
    assert submit_button.is_enabled() is False
    email_form.send_keys("bob.marley@example.com")
    assert submit_button.is_enabled() is True
