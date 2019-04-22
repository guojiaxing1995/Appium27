#coding=utf-8
from selenium.webdriver.common.by import By

from read_ini import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
        self.readini = ReadIni()

    def get_element(self,section,key):
        local = self.readini.get_value(section,key)
        local_by = local.split('>')[0]
        local_value = local.split('>')[1]
        if local_by == 'id':
            return self.driver.find_element_by_id(local_value)
        elif local_by == 'className':
            return self.driver.find_element_by_class_name(local_value)
        elif local_by == 'xpath':
            return self.driver.find_element_by_xpath(local_value)
        elif local_by == 'ANUItext':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+local_value+'")')
        elif local_by == 'ANUIstext':
            return self.driver.find_elements_by_android_uiautomator('new UiSelector().text("'+local_value+'")')
        elif local_by == 'classNames':
            if len(local.split('>')) > 2:
                return self.driver.find_elements_by_class_name(local_value)[int(local.split('>')[2])]
            else:
                return self.driver.find_elements_by_class_name(local_value)
        elif local_by =='ANUIcontent-desc':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().description("'+local_value+'")')
        elif local_by == 'ids':
            if len(local.split('>')) > 2:
                return self.driver.find_elements_by_id(local_value)[int(local.split('>')[2])]
            else:
                return self.driver.find_elements_by_id(local_value)
        else:
            return None
    def get_locator(self,section,key):
        local = self.readini.get_value(section,key)
        local_by = local.split('>')[0]
        local_value = local.split('>')[1]
        if local_by == 'id':
            locator = (By.ID,local_value)
        elif local_by == 'className':
            locator = (By.CLASS_NAME, local_value)
        elif local_by == 'xpath':
            locator = (By.XPATH, local_value)
        elif local_by == 'cssSelector':
            locator = (By.CSS_SELECTOR, local_value)
        elif local_by == 'linkText':
            locator = (By.LINK_TEXT, local_value)
        elif local_by == 'partialLinkText':
            locator = (By.PARTIAL_LINK_TEXT, local_value)
        elif local_by == 'tagName':
            locator = (By.TAG_NAME, local_value)
        else:
            locator =  None

        return locator