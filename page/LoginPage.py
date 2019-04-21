#coding=utf-8
from page.BasePage import BasePage
from util.get_by_local import GetByLocal
from base.PublicMethod import PublicMethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    '''获取登录页面的element'''

    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_carouselfigure_element(self):
        '''获取最后一张轮播图'''
        return self.getByLocal.get_element('login_element','carouselfigure')

    def get_username_element(self):
        '''获取用户名输入框'''
        return self.getByLocal.get_element('login_element','username')

    def get_password_element(self):
        '''获取密码输入框'''
        return self.getByLocal.get_element('login_element','password')

    def get_loginbutton_element(self):
        '''获取登录按钮'''
        return self.getByLocal.get_element('login_element','loginbutton')

    def get_wechat_element(self):
        '''获取微信登录element'''
        return self.getByLocal.get_element('login_element','wechat')

    def get_register_element(self):
        '''获取注册element'''
        return self.getByLocal.get_element('login_element','register')

    def get_forget_element(self):
        '''获取忘记密码element'''
        return self.getByLocal.get_element('login_element','forget')


    def slide(self,direction):
        """
        滑动
        :param direction:
        :return:
        """
        pubMethod = PublicMethod()
        pubMethod.slide(self.driver,direction)

    def get_toast(self,message):
        """获取toast"""
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))