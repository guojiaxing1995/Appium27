#coding=utf-8
from page.DetailPage import DetailPage

class DetailHandle:
    def __init__(self,driver):
        self.driver = driver
        self.detail_page = DetailPage(driver)

    def isDisplay_invoiceDetail(self):
        '''发票详情四个字是否显示'''
        return self.detail_page.get_invoiceDetail_element().is_displayed()

    def isDisplay_reimbButton(self):
        '''报销按钮是否显示'''
        return self.detail_page.get_reimbursement_element().is_displayed()

    def click_tobaccoButton(self):
        '''点击烟酒Button'''
        self.detail_page.get_tobaccoButton_element().click()

    def click_peservationButton(self):
        '''点击保存Button'''
        self.detail_page.get_peservationButton_element().click()

    def click_reimbButton(self):
        '''点击保存Button'''
        self.detail_page.get_reimbursement_element().click()

    def click_previewDownload(self):
        '''点击预览下载'''
        self.detail_page.get_previewDownload_element().click()

    def click_sendEmail(self):
        """点击发票打印按钮"""
        self.detail_page.get_sendEmail_element().click()

    def click_print_(self):
        """点击打印两个字"""
        self.detail_page.get_print_element().click()

    def send_email(self,email):
        '''输入邮箱地址'''
        self.detail_page.get_emailEidtText_element().send_keys(email)

    def click_invoiceCheck(self):
        """点击发票查验"""
        self.detail_page.get_invoiceCheck_element().click()

    def isDisplay_checkPageText(self):
        """发票查验页面可获得"""
        return self.detail_page.get_checkPageText_element().is_displayed()

    def click_remarks(self):
        """点击备注"""
        self.detail_page.get_remarks_element().click()

    def send_remarksEidx(self,remarks):
        '''输入备注'''
        self.detail_page.get_remarksEidx_element().send_keys(remarks)

    def click_peservation(self):
        """点击保存"""
        self.detail_page.get_peservation_element().click()

    def click_customer(self):
        """点击自定义"""
        self.detail_page.get_customer_element().click()

    def send_customerEidx(self,customer):
        """输入自定义待办"""
        self.detail_page.get_customerEidx_element().send_keys(customer)

    def click_deleteText(self):
        """点击删除"""
        self.detail_page.get_deleteText_element().click()

    def click_deleteButton(self):
        """点击删除按钮"""
        self.detail_page.get_deleteButton_element().click()

    def click_reminding(self):
        """点击是否提醒"""
        self.detail_page.get_reminding_element().click()

    def get_date_location(self):
        """获取天数的坐标"""
        elements = self.detail_page.get_dateEidex_element()
        return elements[2].location,elements[2].size

    def swipe_date(self):
        """滑动日期"""
        location_dict,size_dict = self.get_date_location()
        x = location_dict + size_dict['x']/2
        y = int(location_dict['y'])-int(size_dict['y'])
        self.driver.swipe(x,int(location_dict['y']),x,y)

    def click_quxiao(self):
        """点击取消按钮"""
        self.detail_page.get_quxiaoText_element().click()

    def back(self):
        self.detail_page.back()