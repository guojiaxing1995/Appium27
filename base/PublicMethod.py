#coding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PublicMethod:
    def __init__(self):
        pass

    def get_size(self,driver):
        '''获取屏幕尺寸'''
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']

        return width, height

    def slide_up(self,driver):
        '''上滑'''
        width, height = self.get_size(driver)
        driver.swipe(width / 2, height / 10 * 9, width / 2, height / 10 * 1, 2000)

    def slide_left(self,driver):
        '''左滑'''
        width, height = self.get_size(driver)
        driver.swipe(width / 10 * 9, height / 2, width / 10, height / 2, 1000)

    def slide_right(self,driver):
        '''右滑'''
        width, height = self.get_size(driver)
        driver.swipe(width / 10* 9, height / 2, width / 10, height / 2, 1000)

    def slide_down(self,driver):
        '''下滑'''
        width, height = self.get_size(driver)
        driver.swipe(width / 10, height / 2, width / 10 * 9, height / 2, 1000)

    def slide(self,driver,direction):
        '''滑动'''
        if direction == 'left':
            self.slide_left(driver)
        elif direction == 'right':
            self.slide_right(driver)
        elif direction == 'up':
            self.slide_up(driver)
        elif direction == 'down':
            self.slide_down(driver)

    def get_toast(self,driver,message):
        '''获取toast提示'''
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))