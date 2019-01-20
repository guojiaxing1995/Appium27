#coding=utf-8
import os

from handle.WalletHandle import WalletHandle
from handle.ManualHandle import ManualHandle
from handle.DetailHandle import DetailHandle
from handle.HomeHandle import HomeHandle
from util.read_ini import ReadIni
import time,re

class SearchBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.manual_handle = ManualHandle(driver)
        self.wallet_handle = WalletHandle(driver)
        self.detail_handle = DetailHandle(driver)
        self.home_handle = HomeHandle(driver)
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        path = parent_dir + '\config\dataConfig.ini'
        self.readIni = ReadIni(path)

    def serch_all_invoice(self):
        """搜索所有发票"""
        self.home_handle.click_serachInvoice_edittext()
        self.wallet_handle.click_allInvoice()
        time.sleep(3)
        assert self.wallet_handle.get_invoice_size() == 5,'增值税发票发票搜索错误'
        assert self.wallet_handle.get_tarinInvoice_size() == 2,'火车票发票搜索错误'
        assert self.wallet_handle.get_taxiInvoice_size() == 2, '火车票发票搜索错误'

    def serch_paper_invoice(self):
        """搜索纸票"""
        self.home_handle.click_serachInvoice_edittext()
        self.wallet_handle.click_paperInvoice()
        time.sleep(3)
        assert self.wallet_handle.get_invoice_size() == 2, '增值税纸票发票搜索错误'

    def serch_electric_invoice(self):
        """搜索电票"""
        self.home_handle.click_serachInvoice_edittext()
        self.wallet_handle.click_electricInvoice()
        time.sleep(3)
        assert self.wallet_handle.get_invoice_size() == 3, '增值税电票发票搜索错误'

    def serch_train_invoice(self):
        """搜索火车票"""
        self.home_handle.click_serachInvoice_edittext()
        self.manual_handle.click_trainTicket()
        time.sleep(3)
        assert self.wallet_handle.get_tarinInvoice_size() == 3,'火车票搜索错误'

    def serch_taxi_invoice(self):
        """搜索打车票"""
        self.home_handle.click_serachInvoice_edittext()
        self.manual_handle.click_taxiTicket()
        time.sleep(3)
        assert self.wallet_handle.get_taxiInvoice_size()== 3,'打车票搜索错误'

    def accurate_serach(self):
        """精确搜索"""
        peningo_project = self.readIni.get_value('invoice_data', 'ticketOpeningProject_01')
        self.home_handle.send_serachInvoice_edittext(peningo_project)
        self.driver.press_keycode(66)
        time.sleep(3)
        assert self.wallet_handle.get_invoice_size() == 1, '精确搜索错误'

    def vague_serach(self):
        """模糊搜索"""
        peningo_project = self.readIni.get_value('invoice_data', 'ticketOpeningProject_02')
        self.home_handle.send_serachInvoice_edittext(peningo_project)
        self.driver.press_keycode(66)
        time.sleep(3)
        assert self.wallet_handle.get_invoice_size() == 1, '模糊搜索错误'