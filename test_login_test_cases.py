import pytest
import time

from pages.xwiks_page import XwiksPage

link = "https://xwiks.com/"


def test_can_user_sing_in_with_correct_data(browser):
    page = XwiksPage(browser, link)
    page.open_page(page.url)
    page.click_burger_buttom()
    page.click_sign_in_button()

    input_name = browser.find_element_by_xpath("//input[@type='email']")
    input_name.send_keys("pavlik@maillinator.com")
    input_psw = browser.find_element_by_xpath("//input[@type='password']")
    input_psw.send_keys("Qwe123@@")
    stay_in = browser.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple primary--text']")
    stay_in.click()
    singn_button = browser.find_element_by_xpath(
        "//button[@class='btn-purple v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default']")
    singn_button.click()
    time.sleep(10)
    burger_button = browser.find_element_by_css_selector(
        "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
    burger_button.click()
    assert browser.find_element_by_xpath("//span[@class='v-btn__content']")


def test_can_user_login_with_wrong_email(browser):
    browser.get(link)
    time.sleep(2)
    burger_button = browser.find_element_by_css_selector(
        "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
    burger_button.click()
    time.sleep(5)
    sign_in_button = browser.find_element_by_xpath("//div[@class='signup-wrapp']/a")
    sign_in_button.click()
    time.sleep(4)
    input_name = browser.find_element_by_xpath("//input[@type='email']")
    input_name.send_keys("zxczxvzxc@maillinator.com")
    input_psw = browser.find_element_by_xpath("//input[@type='password']")
    input_psw.send_keys("Qwe123@@")
    stay_in = browser.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple primary--text']")
    stay_in.click()
    singn_button = browser.find_element_by_xpath(
        "//button[@class='btn-purple v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default']")
    singn_button.click()
    time.sleep(5)
    frong_email = browser.find_element_by_xpath("//div[@class='v-messages__message']")
    frong_email_true = frong_email.text
    assert "registered" in frong_email_true


def test_can_user_login_with_wrong_password(browser):
    browser.get(link)
    time.sleep(2)
    burger_button = browser.find_element_by_css_selector(
        "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
    burger_button.click()
    time.sleep(5)
    sign_in_button = browser.find_element_by_xpath("//div[@class='signup-wrapp']/a")
    sign_in_button.click()
    time.sleep(4)
    input_name = browser.find_element_by_xpath("//input[@type='email']")
    input_name.send_keys("pavlik@maillinator.com")
    input_psw = browser.find_element_by_xpath("//input[@type='password']")
    input_psw.send_keys("Qwe123@@s")
    stay_in = browser.find_element_by_xpath("//div[@class='v-input--selection-controls__ripple primary--text']")
    stay_in.click()
    singn_button = browser.find_element_by_xpath(
        "//button[@class='btn-purple v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default']")
    singn_button.click()
    time.sleep(5)
    frong_email = browser.find_element_by_xpath("//div[@class='v-messages__message']")
    frong_email_true = frong_email.text
    assert "пароль" in frong_email_true

