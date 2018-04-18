#coding=utf-8
from page.LoginPage import LoginPage

class LoginHandle:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def click_carouselfigure(self):
        '''点击最后一张轮播图'''
        self.login_page.get_carouselfigure_element().click()

    def send_username(self,user):
        '''输入用户名'''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self,password):
        '''输入密码'''
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        '''点击登录'''
        self.login_page.get_loginbutton_element().click()

    def click_register(self):
        '''点击注册'''
        self.login_page.get_register_element().click()

    def click_forget_password(self):
        '''点击忘记密码'''
        self.login_page.get_forget_element().click()

    def slide(self,direction):
        '''滑动'''
        self.login_page.slide(direction)
