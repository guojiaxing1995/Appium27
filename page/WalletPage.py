#coding=utf-8
from util.get_by_local import GetByLocal

class WalletPagePage:
    '''获取票夹页元素'''
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_invoice_num_element(self):
        """获取发票累计"""
        return self.getByLocal.get_element('wallet_element','invoice_num')

    def get_salesParty_element(self):
        """获取销售方三个字"""
        return self.getByLocal.get_element('wallet_element','sales_party')

    def get_deleteButton_element(self):
        """删除按钮"""
        return self.getByLocal.get_element('wallet_element','deleteButton')

    def get_invoiceClass_element(self):
        """获取发票类型按钮"""
        return self.getByLocal.get_element('wallet_element', 'invoiceClass')

    def get_allInvoice_element(self):
        """获取全部两个字"""
        return self.getByLocal.get_element('wallet_element', 'allInvoice')

    def get_paperInvoice_element(self):
        """获取增值税纸质发票"""
        return self.getByLocal.get_element('wallet_element', 'paperInvoice')

    def get_electricInvoice_element(self):
        """获取增值税电子发票"""
        return self.getByLocal.get_element('wallet_element', 'electricInvoice')

    def get_batchOpenIcon_element(self):
        """获取批量操作按钮"""
        return self.getByLocal.get_element('wallet_element', 'batchOpenIcon')

    def get_batchCloseIcon_element(self):
        """获取批量操作收起按钮"""
        return self.getByLocal.get_element('wallet_element', 'batchCloseIcon')

    def get_batchTodoIcon_element(self):
        """获取批量待办按钮"""
        return self.getByLocal.get_element('wallet_element', 'batchTodoIcon')

    def get_batchClassIcon_element(self):
        """获取批量分类按钮"""
        return self.getByLocal.get_element('wallet_element', 'batchClassIcon')

    def get_batchPrintIcon_element(self):
        """获取批量打印按钮"""
        return self.getByLocal.get_element('wallet_element', 'batchPrintIcon')

    def get_selectButton_element(self):
        """获取选择按钮"""
        return self.getByLocal.get_element('wallet_element', 'selectButton')

    def get_printInvoice_element(self):
        """获取打印发票按钮"""
        return self.getByLocal.get_element('wallet_element', 'printInvoice')

    def get_taxiInvoice_element(self):
        """获取打车票三个字"""
        return self.getByLocal.get_element('wallet_element','taxiInvoice')

    def get_tarinInvoice_element(self):
        """获取火车票三个字"""
        return self.getByLocal.get_element('wallet_element','tarinInvoice')