from ui_automation.base.base_page import BasePage

from ui_automation.page_objects.google_home_page.google_home_page_locators import  GooglePageLocators


class GooglePage(BasePage):
    def open_site(self):
        BasePage.get_url(self,GooglePageLocators.ADDRESS)


