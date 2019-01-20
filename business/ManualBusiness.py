#coding=utf-8
import os

from handle.ManualHandle import ManualHandle
from handle.HomeHandle import HomeHandle
from handle.DetailHandle import DetailHandle
from handle.WalletHandle import WalletPagePage
from util.read_ini import ReadIni
import time

class ManualBusiness:
    def __init__(self,driver):
        self.manual_handle = ManualHandle(driver)
        self.home_handle = HomeHandle(driver)
        self.detail_handle = DetailHandle(driver)
        self.wallet_handle = WalletPagePage
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        path = parent_dir + '\config\dataConfig.ini'
        self.readIni = ReadIni(path)

    def enter_manualAdd(self):
        """进入手动新增页面"""
        self.home_handle.click_plusIcon()
        time.sleep(1)
        self.manual_handle.click_manualAdd()

    def manual_add_invoice(self):
        """手动新增增值税发票"""
        # 专票|普票|卷票|红票
        invoice_data = self.readIni.get_value('invoice_data','vatInvoice')
        datas = invoice_data.split('|')
        for data in datas:
            data = data.split(',')
            self.manual_handle.send_invoice_code(data[0])
            self.manual_handle.send_invoice_number(data[1])
            try:
                self.manual_handle.send_invoice_CheckCode(data[2])
            except:
                self.manual_handle.send_invoice_nonTaxPrice(data[2])
            self.manual_handle.click_invoice_data()
            self.manual_handle.send_date(data[3],data[4],data[5])
            #点击确定
            self.manual_handle.click_determine()
            self.manual_handle.click_determine()
            time.sleep(3)
            assert self.detail_handle.isDisplay_reimbButton() == True,"手动新增发票未进入发票详情页"
            self.manual_handle.back()

    def enter_add_train(self):
        """进入手动新增火车票页面"""
        self.manual_handle.click_trainTicket()

    def enter_add_taxi(self):
        """进入手动新增打车票页面"""
        self.manual_handle.click_taxiTicket()

    def manual_add_train(self):
        """手动新增火车票"""
        invoice_data = self.readIni.get_value('invoice_data', 'trainTicket')
        datas = invoice_data.split('|')
        for data in datas:
            data = data.split(',')
            self.manual_handle.send_trainNum(data[0])
            self.manual_handle.click_trainDate()
            self.manual_handle.click_determine()
            self.manual_handle.send_startStation(data[1])
            self.manual_handle.send_endStation(data[2])
            self.manual_handle.send_trainMoney(data[3])
            self.manual_handle.send_trainName(data[4])
            self.manual_handle.click_determine()
            time.sleep(3)
            assert self.detail_handle.isDisplay_reimbButton() == True,"手动新增发票未进入发票详情页"
            self.manual_handle.back()

    def manual_add_taxi(self):
        """手动新增打车票"""
        invoice_data = self.readIni.get_value('invoice_data', 'taxiTicket')
        datas = invoice_data.split('|')
        for data in datas:
            self.manual_handle.send_trainMoney(data)
            self.manual_handle.click_trainDate()
            self.manual_handle.click_determine()
            self.manual_handle.click_determine()
            time.sleep(3)
            assert self.detail_handle.isDisplay_reimbButton() == True, "手动新增发票未进入发票详情页"
            self.manual_handle.back()

    def enter_manualCheck(self):
        """进入手动查验页面"""
        self.home_handle.click_service()
        self.home_handle.click_plusIcon()
        time.sleep(1)
        self.manual_handle.click_manualCheck()

    def manual_check_invoice(self):
        """手动查验增值税发票"""
        # 专票|普票|卷票|红票
        invoice_data = self.readIni.get_value('invoice_data','vatInvoice')
        datas = invoice_data.split('|')
        for data in datas:
            data = data.split(',')
            self.manual_handle.send_invoice_code(data[0])
            self.manual_handle.send_invoice_number(data[1])
            try:
                self.manual_handle.send_invoice_CheckCode(data[2])
            except:
                self.manual_handle.send_invoice_nonTaxPrice(data[2])
            self.manual_handle.click_invoice_data()
            self.manual_handle.send_date(data[3],data[4],data[5])
            #点击确定
            self.manual_handle.click_determine()
            time.sleep(1)
            self.manual_handle.click_CheckButton()
            time.sleep(30)
            #assert self.detail_handle.isDisplay_invoiceDetail() == True,"手动查验发票未进入发票查验页"
            self.manual_handle.back()