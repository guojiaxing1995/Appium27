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

    def test_001_enter_discover(self):
        """进入发现页面"""
        self.bbs_business.switch_bbs()

