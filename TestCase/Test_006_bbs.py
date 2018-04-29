#coding=utf-8
import unittest
from business.BbsBusiness import BbsBusiness
from business.HomeBusiness import HomeBusiness
from TestCase.Test_001_login import Login
import sys,time

class ParameTestCase(unittest.TestCase):
    """
    该类继承unittest  该类的子类可以传参数
    """
    def __init__(self,methodName='runTest',parames=None):
        super(ParameTestCase,self).__init__(methodName)
        global parame
        parame = parames

class BBS(ParameTestCase):
    """
    发票归集
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = Login().driver
        cls.home_business = HomeBusiness(cls.driver)
        cls.bbs_business = BbsBusiness(cls.driver)

    def setUp(self):
        pass

    def test_001_enter_discover(self):
        """进入发现页面"""
        self.bbs_business.switch_bbs()

    def tearDown(self):
        if sys.exc_info()[0]:
            now = time.strftime('%Y-%m-%d-%H_%M_%S')
            self.driver.save_screenshot('../img/'+now+'.jpg')
