from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ui_automation.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Test(BasePage):
    def test_chrome(self):
        try:
            BasePage.get_driver(self,BasePage.appium_server_url,BasePage.capabilities)
            # 寻找单个元素并点击
            element_accept = ("id", "com.android.chrome:id/terms_accept")
            BasePage.is_element_exist(self,element_accept)
            BasePage.find_element_click(self,element_accept)
            element_thanks = ("id","com.android.chrome:id/negative_button")
            BasePage.is_element_exist(self, element_thanks)
            BasePage.find_element_click(self, element_thanks)
            element_no_thanks = ("id","com.android.chrome:id/negative_button")
            BasePage.is_element_exist(self, element_no_thanks)
            BasePage.find_element_click(self, element_no_thanks)
            element_keep_google = ("id", "com.android.chrome:id/button_secondary")
            BasePage.is_element_exist(self, element_keep_google)
            BasePage.find_element_click(self, element_keep_google)
            BasePage.get_url(self,"https://gorest.co.in/")
            self.driver.find_element(By.ID, "com.android.chrome:id/terms_accept").click()
            wait = WebDriverWait(self.driver, 15, 0.5)
            time.sleep(10)
            wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/negative_button")))
            BasePage.get_screenshot(self,"case success")
            #WebDriverWait(self.base, 10).until(lambda x: x.find_element_by_id("com.android.chrome:id/negative_button"))
            self.driver.find_element(By.ID, "com.android.chrome:id/negative_button").click()
            wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/negative_button")))
            #WebDriverWait(self.base, 10).until(lambda x: x.find_element_by_id("com.android.chrome:id/negative_button"))
            self.driver.find_element(By.ID, "com.android.chrome:id/negative_button").click()
            wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/button_secondary")))
            #WebDriverWait(self.base, 10).until(lambda x: x.find_element_by_id("com.android.chrome:id/button_secondary"))
            self.driver.find_element(By.ID, "com.android.chrome:id/button_secondary").click()
            #self.base.get("https://gorest.co.in/")
        except Exception as e:
            BasePage.get_screenshot(self,"case failed")
            raise e
        finally:
            pass



