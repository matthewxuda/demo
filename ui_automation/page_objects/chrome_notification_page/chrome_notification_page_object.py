from ui_automation.base.base_page import BasePage

from ui_automation.page_objects.keep_google_page.keep_google_page_locators import  KeepGooglePageLocators
from ui_automation.page_objects.chrome_notification_page.chrome_notification_page_locators import ChromeNotificationPageLocators


class ChromeNotificationPage(BasePage):
    def go_to_keep_google_page_with_no_thank_button(self):

        element = ChromeNotificationPageLocators.NO_THANKS
        BasePage.find_element_click(self, element)
        expected_element = KeepGooglePageLocators.KEEP_GOOGLE
        BasePage.result_assert(self, expected_element, doc='')
