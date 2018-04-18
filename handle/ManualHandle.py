#coding=utf-8
from page.ManualPage import ManualPage

class ManualHandle:
    def __init__(self,driver):
        self.manual_page = ManualPage(driver)

    def click_manualAdd(self):
        '''点击手动新增输入框'''
        self.manual_page.get_manualAdd_element().click()

    def click_manualCheck(self):
        '''点击手动查验输入框'''
        self.manual_page.get_manualCheck_element().click()

    def send_invoice_code(self,invoice_code):
        '''输入发票代码'''
        self.manual_page.get_inputCode_element().send_keys(invoice_code)

    def send_invoice_number(self,invoice_number):
        '''输入发票号码'''
        self.manual_page.get_inputNumber_element().send_keys(invoice_number)

    def send_invoice_CheckCode(self,invoice_checkcode):
        '''输入发票校验码'''
        self.manual_page.get_inputCheckCode_element().send_keys(invoice_checkcode)

    def send_invoice_nonTaxPrice(self,invoice_nonTaxPrice):
        '''输入发票不含税价'''
        self.manual_page.get_inputNonTaxPrice_element().send_keys(invoice_nonTaxPrice)

    def click_invoice_data(self):
        '''点击开票日期输入框'''
        self.manual_page.get_inputInvoiceDate_element().click()

    def click_determine(self):
        '''点击确认'''
        self.manual_page.get_determine_element().click()

    def send_date(self,year,month,day):
        """输入时间控件的年月日"""
        elements = self.manual_page.get_dateEidex_element()
        elements[0].clear()
        elements[0].send_keys(year)
        elements[1].clear()
        elements[1].send_keys(month)
        elements[2].clear()
        elements[2].send_keys(day)

    def click_trainTicket(self):
        '''点击火车票按钮'''
        self.manual_page.get_trainTicket_element().click()

    def click_taxiTicket(self):
        '''点击打车票按钮'''
        self.manual_page.get_taxiTicket_element().click()

    def send_trainNum(self,trainNum):
        '''输入车次'''
        self.manual_page.get_trainNum_element().send_keys(trainNum)

    def click_trainDate(self):
        '''点击车票日期输入框'''
        self.manual_page.get_trainDate_element().click()

    def send_startStation(self,startStation):
        '''输入始发站'''
        self.manual_page.get_startStation_element().send_keys(startStation)

    def send_endStation(self,endStation):
        '''输入终点站'''
        self.manual_page.get_endStation_element().send_keys(endStation)

    def send_trainMoney(self,trainMoney):
        '''输入车票金额'''
        self.manual_page.get_trainMoney_element().send_keys(trainMoney)

    def send_trainName(self,trainName):
        '''输入车票姓名'''
        self.manual_page.get_trainName_element().send_keys(trainName)

    def click_CheckButton(self):
        '''点击查验Button'''
        self.manual_page.get_checkButton_element().click()


    def back(self):
        self.manual_page.back()
