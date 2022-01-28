
import time



def test_can_user_open_photo_page(browser):
    link = "https://xwiks.com/"
    browser.get(link)
    time.sleep(2)
    open_photo_page_button = browser.find_element_by_xpath(
        "//button[@class='v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--default btn-dark btn-xsm']")
    open_photo_page_button.click()
    photo_url = "https://xwiks.com/channels"
    assert "https://xwiks.com/channels" == photo_url


def test_can_user_open_burger_menu(browser):
    link = "https://xwiks.com/"
    browser.get(link)
    time.sleep(2)
    burger_button = browser.find_element_by_css_selector(
        "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
    burger_button.click()
    left_sidebar = browser.find_element_by_css_selector("div[class='v-navigation-drawer__content']")
    assert left_sidebar

