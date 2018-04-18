#coding=utf-8
import unittest
from business.ManualBusiness import ManualBusiness
from business.HomeBusiness import HomeBusiness
from business.WalletBusiness import WalletBusiness
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

class BatchOperation(ParameTestCase):
    """
    批量操作
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = Login().driver
        cls.home_business = HomeBusiness(cls.driver)
        cls.manual_business = ManualBusiness(cls.driver)
        cls.wallet_business = WalletBusiness(cls.driver)

    def setUp(self):
        pass

    def test_001_batchIcon_open_close(self):
        """批量操作按钮弹出收起成功"""
        self.wallet_business.batchIcon_open_close()

    def test_002_batch_class(self):
        """批量选择分类"""
        self.wallet_business.batch_class()

    def test_003_batch_boto(self):
        """批量选择待办"""
        self.wallet_business.batch_todo()

    def test_004_batch_print(self):
        """批量打印"""
        self.wallet_business.batch_print()

    def test_005_printpage_print(self):
        """批量打印页面打印发票"""
        self.wallet_business.printpage_print()

    def test_006_printpage_print(self):
        """批量打印页面打印发票"""
        self.wallet_business.send_email()
        self.driver.back()
