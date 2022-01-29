# from .pages.selenium1py import Selenium1py
from pages.selenium1py import Selenium1py


def test_guest_can_go_to_login_page(browser):
    main_link = "http://selenium1py.pythonanywhere.com/"
    page = Selenium1py(browser, main_link)
    page.open_page(page.url)
    page.go_to_login_page()
    return
