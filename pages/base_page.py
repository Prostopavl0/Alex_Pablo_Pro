from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url):
        self.browser = browser
        self.url = url

    def open_page(self, url):
        self.browser.get(url)