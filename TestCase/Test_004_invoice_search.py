#coding=utf-8

from TestCase import ParameTestCase
from business.SearchBusiness import SearchBusiness
from business.HomeBusiness import HomeBusiness
from business.WalletBusiness import WalletBusiness
import sys,time


class InvoiceSearch(ParameTestCase):
    """
    发票搜索
    """
    @classmethod
    def setUpClass(cls):
        cls.home_business = HomeBusiness(cls.driver)
        cls.search_business = SearchBusiness(cls.driver)
        cls.wallet_business = WalletBusiness(cls.driver)


    def test_001_search_all(self):
        """搜索全部发票"""
        self.home_business.enter_home()
        self.search_business.serch_all_invoice()

    def test_002_search_paper(self):
        """搜索纸票"""
        self.search_business.serch_paper_invoice()

    def test_003_search_eletric(self):
        """搜索电票"""
        self.search_business.serch_electric_invoice()

    def test_004_search_train(self):
        """搜索火车票"""
        self.search_business.serch_train_invoice()

    def test_005_search_taxi(self):
        """搜索打车票"""
        self.search_business.serch_taxi_invoice()

    def test_006_accurate_serach(self):
        """精确搜索"""
        self.search_business.accurate_serach()

    def test_007_vague_serach(self):
        """模糊搜索"""
        self.search_business.vague_serach()

