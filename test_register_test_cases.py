import time
import random

link = "https://xwiks.com/"


def user_name():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    names = ""
    for x in range(7):
        letter = random.sample(letters, 1)[0]
        names += letter
    names += "user"
    return names


def random_email():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    email = ""
    for x in range(7):
        letter = random.sample(letters, 1)[0]
        email += letter
    email += "@gmail.com"
    return email


def test_can_user_register_via_viewer(browser):
    name = user_name()
    email = random_email()
    browser.get(link)
    time.sleep(2)
    burger_button = browser.find_element_by_css_selector(
        "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
    burger_button.click()
    time.sleep(5)
    sign_in_button = browser.find_element_by_xpath("//div[@class='signup-wrapp']/a")
    sign_in_button.click()
    time.sleep(4)
    create_account_button = browser.find_element_by_xpath("//div[@class='text-center']/a")
    create_account_button.click()
    time.sleep(5)
    input_user_name = browser.find_element_by_xpath(
        "//form[@class='v-form']/span[@label='User name']/div/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-text-field__slot']/input")
    input_user_name.send_keys(name)
    time.sleep(6)
    input_email_address = browser.find_element_by_xpath(
        "//span[@label='Email']/div/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-text-field__slot']/input")
    input_email_address.send_keys(email)
    time.sleep(4)
    input_password = browser.find_element_by_xpath(
        "//span[@label='Password']/div/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-text-field__slot']/input")
    input_password.send_keys("Qwe123@@")
    sing_up_button = browser.find_element_by_xpath("//div[@class='btn-center']/button")
    sing_up_button.click()
    time.sleep(5)
    assert browser.find_element_by_xpath("//span[@class='v-btn__content']")
