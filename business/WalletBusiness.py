#coding=utf-8
from handle.WalletHandle import WalletHandle
from handle.DetailHandle import DetailHandle
from handle.ManualHandle import ManualHandle
from handle.HomeHandle import HomeHandle
import time,re

class WalletBusiness:
    def __init__(self,driver):
        self.wallet_handle = WalletHandle(driver)
        self.detail_handle = DetailHandle(driver)
        self.manual_handle = ManualHandle(driver)
        self.home_handle = HomeHandle(driver)

    def get_invoice_num(self):
        num_text = self.wallet_handle.get_invoice_num()
        num_text = re.findall('累计发票：(.*)张',num_text)[0]
        num = int(num_text)

        return num

    def swipe_invoice_delete(self,n):
        """滑动增值税发票删除"""
        for i in range(0,n):
            self.wallet_handle.get_sales_party_coordinate()

    def choose_paperInvoice_delete(self):
        """筛选出增值税纸票删除"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_paperInvoice()
        time.sleep(4)
        self.swipe_invoice_delete(2)
        self.wallet_handle.click_paperInvoice()
        self.wallet_handle.click_allInvoice()
        time.sleep(2)

    def choose_electricInvoice_delete(self):
        """筛选出增值税电票删除"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_electricInvoice()
        time.sleep(4)
        self.swipe_invoice_delete(2)
        self.wallet_handle.click_electricInvoice()
        self.wallet_handle.click_allInvoice()
        time.sleep(2)

    def batchIcon_open_close(self):
        """批量操作按钮弹出 收起"""
        self.wallet_handle.click_batchOpenIcon()
        self.wallet_handle.click_batchCloseIcon()

    def batch_class(self):
        """批量选择分类"""
        self.wallet_handle.click_batchOpenIcon()
        self.wallet_handle.click_batchClassIcon()
        self.wallet_handle.click_selectButton()
        self.manual_handle.click_determine()
        #选择分类烟酒
        self.detail_handle.click_tobaccoButton()
        #点击保存
        self.detail_handle.click_peservationButton()
        #点击确定
        self.manual_handle.click_determine()
        time.sleep(2)

    def batch_todo(self):
        """批量选择待办"""
        self.wallet_handle.click_batchOpenIcon()
        self.wallet_handle.click_batchTodoIcon()
        self.wallet_handle.click_selectButton()
        self.manual_handle.click_determine()
        #选择待办报销
        self.detail_handle.click_reimbButton()
        #点击保存
        self.detail_handle.click_peservationButton()
        #点击确定
        #self.manual_handle.click_determine()
        time.sleep(2)

    def batch_print(self):
        """批量打印"""
        self.wallet_handle.click_batchOpenIcon()
        self.wallet_handle.click_batchPrintIcon()
        self.wallet_handle.click_selectButton()
        self.manual_handle.click_determine()
        time.sleep(12)

    def printpage_print(self):
        """批量打印页面点击打印"""
        self.wallet_handle.click_printInvoice()
        self.home_handle.click_confirm()


    def send_email(self):
        """批量打印页面发送邮箱"""
        self.detail_handle.click_sendEmail()
        self.detail_handle.send_email('302802003@qq.com')
        self.home_handle.click_confirm()
        time.sleep(3)

    def eInvoice_choose_all(self):
        """票夹电票页面筛选全部发票"""
        self.wallet_handle.click_electricInvoice()
        self.wallet_handle.click_allInvoice()
        time.sleep(4)

    def paper_choose_all(self):
        """票夹纸票页面筛选全部发票"""
        self.wallet_handle.click_paperInvoice()
        self.wallet_handle.click_allInvoice()
        time.sleep(4)

    def taxi_choose_all(self):
        """票夹打车票页面筛选全部发票"""
        self.wallet_handle.click_taxi()
        self.wallet_handle.click_allInvoice()
        time.sleep(4)

    def train_choose_all(self):
        """票夹火车票页面筛选全部发票"""
        self.wallet_handle.click_train()
        self.wallet_handle.click_allInvoice()
        time.sleep(4)

    def choose_eInvoice_enter(self):
        """筛选出电票，点击进入一张电票"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_electricInvoice()
        time.sleep(4)
        self.wallet_handle.click_invoice()

    def choose_paperInvoice_enter(self):
        """筛选出纸票，点击进入一张纸票"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_paperInvoice()
        time.sleep(4)
        self.wallet_handle.click_invoice()

    def choose_train_enter(self):
        """筛选出火车票，点击进入一张火车票"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_train()
        time.sleep(4)
        self.wallet_handle.click_train_invoice()

    def choose_taxi_enter(self):
        """筛选出打车票，点击进入一张打车票"""
        self.wallet_handle.click_invoiceClass()
        self.wallet_handle.click_taxi()
        time.sleep(4)
        self.wallet_handle.click_taxi_invoice()