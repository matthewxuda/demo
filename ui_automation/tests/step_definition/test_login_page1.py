import appium
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.chrome',
    appActivity='com.google.android.apps.chrome.Main',
    language='en',
    locale='US'
)
appium_server_url = 'http://127.0.0.1:4723/wd/hub'
class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

        self.driver.get("https://gorest.co.in/")

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_chrome(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.android.chrome:id/image"]')
        el.click()

if __name__ == '__main__':
    unittest.main()
