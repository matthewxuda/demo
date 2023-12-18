from ui_automation.base.base_page import BasePage

from ui_automation.page_objects.turn_on_sync_page.turn_on_sync_page_locators import  TurnOnSyncPageLocators
from ui_automation.page_objects.welcome_page.welcome_page_locators import WelcomPageLocators

class WelcomePageObject(BasePage):
    def launch_chrome(self):
        BasePage.get_driver(self, BasePage.appium_server_url, BasePage.capabilities)

    def check_welcome_page(self):
        expected_element =WelcomPageLocators.NO_THANKS
        BasePage.result_assert(self, expected_element, doc='')

    def go_to_welcome_page_with_no_thank_button(self):
        element = WelcomPageLocators.NO_THANKS
        BasePage.find_element_click(self, element)
        expected_element =TurnOnSyncPageLocators.NO_THANKS
        BasePage.result_assert(self, expected_element, doc='')
