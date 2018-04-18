#coding=utf-8

from handle.DetailHandle import DetailHandle
from handle.WalletHandle import WalletHandle
from handle.ManualHandle import ManualHandle
from handle.HomeHandle import HomeHandle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DetailBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.detail_handle = DetailHandle(driver)
        self.wallet_handle = WalletHandle(driver)
        self.home_handle = HomeHandle(driver)
        self.manual_handle = ManualHandle(driver)

    def enter_preview_download(self):
        """进入预览下载页面"""
        self.detail_handle.click_previewDownload()

    def ele_invoice_print(self):
        """电票打印"""
        self.detail_handle.click_print_()
        self.home_handle.click_confirm()

    def send_email(self):
        """电票发送邮箱"""
        self.detail_handle.click_sendEmail()
        self.detail_handle.send_email('302802003@qq.com')
        self.home_handle.click_confirm()
        time.sleep(3)

    def eleInvoice_check(self):
        """电票查验"""
        self.detail_handle.click_invoiceCheck()
        time.sleep(10)
        assert self.detail_handle.isDisplay_checkPageText() == True,"进入查验页面失败"
        self.driver.back()

    def invoice_remarks(self):
        """发票备注"""
        self.detail_handle.click_remarks()
        self.detail_handle.send_remarksEidx('备注发票Invoice')
        self.detail_handle.click_peservation()
        e = self.driver.find_elements_by_xpath("//*[contains(@text,备注发票Invoice)]")
        assert e.is_displayed() == True,"添加备注失败"

    def customer_need_do(self):
        """新建自定待办"""
        self.detail_handle.click_customer()
        self.detail_handle.send_customerEidx('1234')
        self.manual_handle.click_determine()
        e = self.driver.find_elements_by_xpath("//*[contains(@text,1234)]")
        assert e.is_displayed() == True, "添加自定义待办失败"

    def cusromer_delete(self):
        """删除自定义待办"""
        self.detail_handle.click_deleteText()
        self.detail_handle.click_deleteButton()
        self.manual_handle.click_determine()
        e = self.driver.find_elements_by_xpath("//*[contains(@text,1234)]")
        assert e.is_displayed() == False, "删除自定义待办失败"

    def add_jiyiji(self):
        """添加记一记"""
        self.detail_handle.click_reminding()
        self.manual_handle.click_determine()
        self.detail_handle.swipe_date()
        self.manual_handle.click_determine()
        jiyiji_text = ("xpath", "//*[contains(@text,您有一张)]")
        WebDriverWait(self.driver, 180, 0.1).until(EC.presence_of_element_located(jiyiji_text))
        self.detail_handle.click_quxiao()

    def delete_invoice(self):
        """详情页删除发票"""
        self.detail_handle.click_deleteButton()
        self.manual_handle.click_determine()



