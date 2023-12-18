from ui_automation.base.base_page import BasePage

from ui_automation.page_objects.keep_google_page.keep_google_page_locators import  KeepGooglePageLocators
from ui_automation.page_objects.google_home_page.google_home_page_locators import GooglePageLocators


class KeepGooglePage(BasePage):
    def go_to_google_page_with_no_thank_button(self):

        element = KeepGooglePageLocators.KEEP_GOOGLE
        BasePage.find_element_click(self, element)
        expected_element = GooglePageLocators.LOGO
        BasePage.result_assert(self, expected_element, doc='')
