#coding=utf-8
from page.WalletPage import WalletPagePage
from page.ManualPage import ManualPage
import time
class WalletHandle:
    def __init__(self,driver):
        self.driver = driver
        self.wallet_page = WalletPagePage(driver)
        self.manual_page = ManualPage(driver)

    def click_invoiceClass(self):
        """点击发票类型"""
        self.wallet_page.get_invoiceClass_element().click()

    def click_paperInvoice(self):
        """点击增值税纸质发票"""
        self.wallet_page.get_paperInvoice_element().click()

    def click_electricInvoice(self):
        """点击增值税电子发票"""
        self.wallet_page.get_electricInvoice_element().click()

    def click_allInvoice(self):
        """点击全部按钮"""
        self.wallet_page.get_allInvoice_element().click()

    def get_invoice_num(self):
        """获取发票累计的文本值"""
        a = self.wallet_page.get_invoice_num_element().text
        a = a.encode('unicode-escape').decode('string_escape')
        return self.wallet_page.get_invoice_num_element().get_attribute('name')

    def click_invoice(self):
        """点击增值税发票"""
        elements = self.wallet_page.get_salesParty_element()
        elements[0].click()

    def click_train(self):
        """点击火车票"""
        elements = self.wallet_page.get_tarinInvoice_element()
        elements[0].click()

    def click_taxi(self):
        """点击打车票"""
        elements = self.wallet_page.get_taxiInvoice_element()
        elements[0].click()

    def click_train_invoice(self):
        """点击火车票"""
        elements = self.wallet_page.get_tarinInvoice_element()
        elements[1].click()

    def click_taxi_invoice(self):
        """点击打车票"""
        elements = self.wallet_page.get_taxiInvoice_element()
        elements[1].click()

    def get_invoice_number(self):
        """获取增值税发票张数"""
        elements = self.wallet_page.get_salesParty_element()
        return len(elements)

    def get_taxiInvoice_num(self):
        """获取打车票张数"""
        elements = self.wallet_page.get_taxiInvoice_element()
        return len(elements)

    def get_tarinInvoice_num(self):
        """获取火车票张数"""
        elements = self.wallet_page.get_tarinInvoice_element()
        return len(elements)

    def get_sales_party_coordinate(self):
        """获取票夹发票销售方的坐标,滑动"""
        elements = self.wallet_page.get_salesParty_element()
        for element in elements:
            location_dict = element.location
            self.driver.swipe(int(location_dict['x'])*8,int(location_dict['y']),0,int(location_dict['y']),2000)
            time.sleep(1)
            #点击删除按钮
            self.click_deleteButton()
            #点击确定
            self.manual_page.get_determine_element().click()
            time.sleep(3)
            break

    def click_deleteButton(self):
        """点击删除按钮"""
        self.wallet_page.get_deleteButton_element().click()

    def click_batchOpenIcon(self):
        """点击批量操作按钮"""
        self.wallet_page.get_batchOpenIcon_element().click()

    def click_batchCloseIcon(self):
        """点击批量操作关闭按钮"""
        self.wallet_page.get_batchCloseIcon_element().click()

    def click_batchTodoIcon(self):
        """点击批量待办按钮"""
        self.wallet_page.get_batchTodoIcon_element().click()

    def click_batchClassIcon(self):
        """点击批量分类按钮"""
        self.wallet_page.get_batchClassIcon_element().click()

    def click_batchPrintIcon(self):
        """点击批量打印按钮"""
        self.wallet_page.get_batchPrintIcon_element().click()

    def click_selectButton(self):
        """循环点击选择按钮"""
        selectButtons = self.wallet_page.get_selectButton_element()
        for selectButton in selectButtons:
            selectButton.click()

    def click_printInvoice(self):
        """点击发票打印按钮"""
        self.wallet_page.get_printInvoice_element().click()

