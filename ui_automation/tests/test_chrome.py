from ui_automation.base.base_page import BasePage

class Test(BasePage):
    def test_chrome(self):
        try:
            BasePage.get_driver(self,BasePage.appium_server_url,BasePage.capabilities)
            element_accept = ("id", "com.android.chrome:id/terms_accept")
            BasePage.find_element_click(self,element_accept)
        except Exception as e:
            BasePage.get_screenshot(self,"")
            raise e
        finally:
            pass



