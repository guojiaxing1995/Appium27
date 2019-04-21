#coding=utf-8
from page.BasePage import BasePage
from util.get_by_local import GetByLocal



class ManualPage(BasePage):
    '''获取手动归集页面元素'''
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_manualAdd_element(self):
        """获取手动新增按钮"""
        return self.getByLocal.get_element('manual_element','manualAdd')

    def get_manualCheck_element(self):
        """获取手动查验按钮"""
        return self.getByLocal.get_element('manual_element','manualCheck')

    def get_inputCode_element(self):
        """获取发票代码输入框"""
        return self.getByLocal.get_element('manual_element','inputCode')

    def get_inputNumber_element(self):
        """获取发票号码输入框"""
        return self.getByLocal.get_element('manual_element','inputNumber')

    def get_inputCheckCode_element(self):
        """获取发票校验码输入框"""
        return self.getByLocal.get_element('manual_element','inputCheckCode')

    def get_inputNonTaxPrice_element(self):
        """获取不含税价输入框"""
        return self.getByLocal.get_element('manual_element','inputNonTaxPrice')

    def get_inputInvoiceDate_element(self):
        """获取开票日期输入框"""
        return self.getByLocal.get_element('manual_element','inputInvoiceDate')

    def get_determine_element(self):
        """获取确定按钮"""
        return self.getByLocal.get_element('manual_element','determine')

    def get_dateEidex_element(self):
        """获取增票日期控件选择框（年月日）"""
        return self.getByLocal.get_element('manual_element','dateEidex')

    def get_trainTicket_element(self):
        """获取火车票按钮"""
        return self.getByLocal.get_element('manual_element','trainTicket')

    def get_taxiTicket_element(self):
        """获取打车票按钮"""
        return self.getByLocal.get_element('manual_element','taxiTicket')

    def get_trainNum_element(self):
        """获取车次输入框"""
        return self.getByLocal.get_element('manual_element','trainNum')

    def get_trainDate_element(self):
        """获取车票日期输入框"""
        return self.getByLocal.get_element('manual_element','trainDate')

    def get_startStation_element(self):
        """获取始发站输入框"""
        return self.getByLocal.get_element('manual_element','startStation')

    def get_endStation_element(self):
        """获取终点站输入框"""
        return self.getByLocal.get_element('manual_element','endStation')

    def get_trainMoney_element(self):
        """获取车票金额输入框"""
        return self.getByLocal.get_element('manual_element','trainMoney')

    def get_trainName_element(self):
        """获取车票姓名输入框"""
        return self.getByLocal.get_element('manual_element','trainName')

    def get_checkButton_element(self):
        """获取查验按钮"""
        return self.getByLocal.get_element('manual_element','checkButton')



    def back(self):
        """返回"""
        self.driver.back()