from pytest import fixture
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from email.header import decode_header
import imaplib
import email
import re
import os


@fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


@fixture
def no_reply():
    return os.environ.get("PASSWORDLESS_EMAIL_NOREPLY_ADDRESS", "noreply.shoppe.app@gmail.com")


@fixture
def creds_email():
    login = os.environ.get("EMAIL_TEST_LOGIN")
    password = os.environ.get("EMAIL_TEST_PASSWORD")
    return login, password


@fixture
def imap_server():
    imap = os.environ.get("IMAP_SERVER")
    return imap


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


def test_log_in(driver, base_url, no_reply, creds_email, imap_server):
    driver.get(base_url + "/login")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    email_form = driver.find_element(By.ID, "mat-input-1")
    email_form.send_keys(creds_email[0])

    assert submit_button.is_enabled() is True

    submit_button.click()
    driver.implicitly_wait(2)
    modal_form = driver.find_element(By.TAG_NAME, "app-auth-modal")
    modal_form_input = modal_form.find_element(By.TAG_NAME, "input")
    modal_form_submit_button = modal_form.find_element(By.CSS_SELECTOR, "button[type='submit']")

    assert modal_form is not None
    assert creds_email[0] in modal_form.text

    code_re = re.compile(r"Enter this token to sign in: (\d{6})")
    with imaplib.IMAP4_SSL(imap_server) as imap:
        imap.login(creds_email[0], creds_email[1])
        status, messages = imap.select("INBOX")
        last_message = str(messages[0].decode())
        res, msg = imap.fetch(last_message, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                from_, encoding = decode_header(msg.get("From"))[0]
                if isinstance(from_, bytes):
                    from_ = from_.decode(encoding)
                assert from_ == no_reply
        code_result = code_re.search(str(msg))
        code = code_result.groups()[0]
        assert len(code) == 6
    modal_form_input.click()
    modal_form_input.send_keys("202020-asd';.2#")
    assert modal_form_submit_button.is_enabled() is False
    modal_form_input.send_keys("23233")
    assert modal_form_submit_button.is_enabled() is False
    modal_form_input.send_keys("2020204")
    assert modal_form_submit_button.is_enabled() is False
    modal_form_input.send_keys("dfdfdf")
    assert modal_form_submit_button.is_enabled() is False

    modal_form_input.clear()
    modal_form_input.send_keys(132344)

    assert modal_form_submit_button.is_enabled() is True

    modal_form_submit_button.submit()
    #
    # wait = WebDriverWait(driver, 3)
    # wait.until(lambda d: driver.current_url != f"{base_url}/my-profile")

    # assert driver.current_url.endswith("/my-profile")





