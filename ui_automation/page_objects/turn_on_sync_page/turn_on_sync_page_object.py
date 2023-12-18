from ui_automation.base.base_page import BasePage

from ui_automation.page_objects.turn_on_sync_page.turn_on_sync_page_locators import  TurnOnSyncPageLocators
from ui_automation.page_objects.chrome_notification_page.chrome_notification_page_locators import ChromeNotificationPageLocators

class TurnOnSyncPageObject(BasePage):
    def go_to_chrome_notification_page_with_no_thank_button(self):

        element = TurnOnSyncPageLocators.NO_THANKS
        BasePage.find_element_click(self, element)
        expected_element =ChromeNotificationPageLocators.NO_THANKS
        BasePage.result_assert(self, expected_element, doc='')
