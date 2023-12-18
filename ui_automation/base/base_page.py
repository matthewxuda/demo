import datetime

import allure
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional, Dict, Tuple, Union
from appium import webdriver
import logger
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import pytest_bdd
from selenium.webdriver.support.wait import WebDriverWait

#Optional[Dict]
class BasePage:
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
    wait_seconds = 30
    frequency = 0.5



    def get_driver(self, command_executor: str, capabilities):
        self.driver = webdriver.Remote(command_executor, options=UiAutomator2Options().load_capabilities(capabilities))
        return self.driver

    def get_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise e
        finally:
            pass

    def is_element_exist(self, element, wait_seconds,frequency, doc=''):
        """
        判断元素是否存在
        """
        by = element[0]
        value = element[1]
        try:
            if by == "id":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.ID, value)))
            elif by == "name":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.NAME, value)))
            elif by == "class":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif by == "text":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif by == "partial_text":
                WebDriverWait(self.driver, wait_seconds,frequency).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            elif by == "xpath":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.XPATH, value)))
            elif by == "css":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            elif by == "tag":
                WebDriverWait(self.driver, wait_seconds,frequency).until(EC.presence_of_element_located((By.TAG_NAME, value)))
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
        except:
            self.get_screenshot(doc)
            return False
        return True


    def find_element_click(self, element: Tuple[str, Union[str, Dict]],doc=''):
        """
        寻找元素
        """
        by = element[0]
        value = element[1]
        try:
            if self.is_element_exist(element, BasePage.wait_seconds,BasePage.frequency,doc):
                if by == "id":
                    self.driver.find_element(By.ID, value).click()
                elif by == "name":
                    return self.driver.find_element(By.NAME, value).click()
                elif by == "class":
                    return self.driver.find_element(By.CLASS_NAME, value).click()
                elif by == "text":
                    return self.driver.find_element(By.LINK_TEXT, value).click()
                elif by == "partial_text":
                    return self.driver.find_element(By.PARTIAL_LINK_TEXT, value).click()
                elif by == "xpath":
                    return self.driver.find_element(By.XPATH, value).click()
                elif by == "css":
                    return self.driver.find_element(By.CSS_SELECTOR, value).click()
                elif by == "tag":
                    return self.driver.find_element(By.TAG_NAME, value).click()
                else:
                    raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
        except Exception as e:
            screen_name = self.get_screenshot(doc)
            raise e

    def find_elements(self, element: Tuple[str, Union[str, Dict]], doc=''):
        """
        寻找一组元素
        """
        by = element[0]
        value = element[1]
        try:
            if self.is_element_exist(element, BasePage.wait_seconds,BasePage.frequency,doc):
                if by == "id":
                    return self.driver.find_elements(By.ID, value)
                elif by == "name":
                    return self.driver.find_elements(By.NAME, value)
                elif by == "class":
                    return self.driver.find_elements(By.CLASS_NAME, value)
                elif by == "text":
                    return self.driver.find_elements(By.LINK_TEXT, value)
                elif by == "partial_text":
                    return self.driver.find_elements(By.PARTIAL_LINK_TEXT, value)
                elif by == "xpath":
                    return self.driver.find_elements(By.XPATH, value)
                elif by == "css":
                    return self.driver.find_elements(By.CSS_SELECTOR, value)
                elif by == "tag":
                    return self.driver.find_elements(By.TAG_NAME, value)
                else:
                    raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
        except Exception as e:
            screen_name = self.get_screenshot(doc)
            logger.error(">>>>>>>> failed to find elements: %s is %s. Error: %s" % (by, value, e))

    def find_all_child_element_by_xpath(self, element: Tuple[str, Union[str, Dict]]):
        """
        寻找元素的所有子元素
        """
        by = element[0]
        value = element[1]
        try:
            if self.is_element_exist(element, BasePage.wait_seconds,BasePage.frequency,doc):
                if by == "xpath":
                    child_value = value + '/child::*'
                    return self.driver.find_elements(By.XPATH, child_value)
                else:
                    raise NameError("Please enter the correct targeting elements 'xpath'.")
        except Exception as e:
            logger.error(">>>>>>>> failed to find elements: %s is %s. Error: %s" % (by, value, e))

    def get_screenshot(self, doc):
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        pic_name = "screenshots/"+now + '.png'
        self.driver.get_screenshot_as_file(pic_name)
        with open(pic_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, doc, allure.attachment_type.PNG)
        return pic_name

    def result_assert(self, expected, doc=''):
        try:
            if self.is_element_exist(expected, BasePage.wait_seconds,BasePage.frequency,doc):
                assert True
            else:
                self.get_screenshot(doc)
                assert False
        except AssertionError:
            self.get_screenshot(doc)
            raise