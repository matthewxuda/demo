from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ui_automation.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# message=""可以省略，注意此时By.ID有两层（）
# element = waite.until(EC.presence_of_element_located((By.ID, "android:id/button1"))
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



