#coding=utf-8
from TestCase import ParameTestCase
from business.LoginBusiness import LoginBusiness
from business.HomeBusiness import HomeBusiness



class Login(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_business = LoginBusiness(cls.driver)
        cls.home_business = HomeBusiness(cls.driver)

    def test_001_slide_carouselfigure(self):
        '''滑动轮播图'''
        self.login_business.slide_carouselfigure()

    def test_002_phone_num_login(self):
        '''登录成功'''
        self.login_business.login_pass()
        #登录后进入首页成功获取底部加号
        self.assertEqual(self.home_business.get_plusIcon(),True)

