#coding=utf-8
import unittest

from TestCase import ParameTestCase
from business.ManualBusiness import ManualBusiness
from business.HomeBusiness import HomeBusiness
from business.WalletBusiness import WalletBusiness
import sys,time

class InvoiceCollection(ParameTestCase):
    """
    发票归集
    """
    @classmethod
    def setUpClass(cls):
        cls.home_business = HomeBusiness(cls.driver)
        cls.manual_business = ManualBusiness(cls.driver)
        cls.wallet_business = WalletBusiness(cls.driver)

    def test_001_enter_add_scan(self):
        """进入新增扫一扫页面"""
        self.home_business.enter_add_scan()
        #若未获取权限,允许获得权限
        self.home_business.judge_has_Jurisdiction()
        self.assertEqual(self.home_business.get_scanOneScan(),True)
        self.driver.back()

    # def test_002_album_distinguish_QRcode(self):
    #     """相册识别二维码"""
    #     self.home_business.album_distinguish_QRcode()

    # def test_002_enter_take_add_photo(self):
    #     """进入新增拍照页面"""
    #     self.home_business.enter_add_take_photo()

    def test_002_enter_manualInput(self):
        """进入手动新增页面"""
        self.home_business.enter_service()
        global invoice_num
       # invoice_num = self.wallet_business.get_invoice_num()
        self.manual_business.enter_manualAdd()

    def test_003_manual_add_invoice(self):
        """手动新增四张增值税发票(专票|普票|卷票|红票)"""
        self.manual_business.manual_add_invoice()

    def test_004_enter_addTrain(self):
        """进入手动新增火车票页面"""
        self.manual_business.enter_add_train()

    def test_005_manual_add_train(self):
        """手动新增火车票"""
        self.manual_business.manual_add_train()

    def test_006_enter_addTiax(self):
        """进入手动新增打车票页面"""
        self.manual_business.enter_add_taxi()

    def test_007_manual_add_taxi(self):
        """手动新增打车票"""
        self.manual_business.manual_add_taxi()
        self.driver.back()
        #self.assertEqual(invoice_num+8,self.wallet_business.get_invoice_num())

    def test_008_wallet_delete_invoice(self):
        """票夹删除增值税发票"""
        time.sleep(10)
        self.wallet_business.choose_electricInvoice_delete()
        self.wallet_business.choose_paperInvoice_delete()


    def test_009_enter_manaualCheck(self):
        """进入手动查验页"""
        self.manual_business.enter_manualCheck()

    def test_010_manaualCheck(self):
        """手动查验四张增值税发票(专票|普票|卷票|红票)"""
        self.manual_business.manual_check_invoice()
        self.driver.back()

    def test_011_weChatBag_add(self):
        """微信卡包归集发票"""
        self.home_business.weChatBag_add()



