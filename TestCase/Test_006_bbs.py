#coding=utf-8

from TestCase import ParameTestCase
from business.BbsBusiness import BbsBusiness
from business.HomeBusiness import HomeBusiness
import sys,time

class BBS(ParameTestCase):
    """
    发票归集
    """
    @classmethod
    def setUpClass(cls):
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
