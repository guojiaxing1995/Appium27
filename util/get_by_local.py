#coding=utf-8
from read_ini import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,section,key):
        readini = ReadIni()
        local = readini.get_value(section,key)
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