#coding=utf-8
import unittest
from business.LoginBusiness import LoginBusiness
from business.HomeBusiness import HomeBusiness
from base.BaseDriver import BaseDriver
import sys,time


class ParameTestCase(unittest.TestCase):
    """
    该类继承unittest  该类的子类可以传参数
    """
    def __init__(self,methodName='runTest',parames=None):
        super(ParameTestCase,self).__init__(methodName)
        global parame
        parame = parames

class Login(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        baseDriver = BaseDriver()
        cls.driver = baseDriver.get_android_driver(parame)
        cls.login_business = LoginBusiness(cls.driver)
        cls.home_business = HomeBusiness(cls.driver)

    def setUp(self):
        pass

    def runTest(self):
        pass

    def test_001_slide_carouselfigure(self):
        '''滑动轮播图'''
        self.login_business.slide_carouselfigure()

    def test_002_phone_num_login(self):
        '''登录成功'''
        self.login_business.login_pass()
        #登录后进入首页成功获取底部加号
        self.assertEqual(self.home_business.get_plusIcon(),True)

    def tearDown(self):
        if sys.exc_info()[0]:
            now = time.strftime('%Y-%m-%d-%H_%M_%S')
            self.driver.save_screenshot('../img/'+now+'.jpg')