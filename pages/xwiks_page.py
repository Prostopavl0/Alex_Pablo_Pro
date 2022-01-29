from .base_page import BasePage


class XwiksPage(BasePage):
    def click_burger_buttom(self):
        burger_button = self.browser.find_element_by_css_selector(
            "button[class='v-app-bar__nav-icon icon-menu v-btn v-btn--icon v-btn--round theme--dark v-size--default']")
        burger_button.click()

    def click_sign_in_button(self):
        sign_in_button = self.browser.find_element_by_xpath("//div[@class='signup-wrapp']/a")
        sign_in_button.click()
