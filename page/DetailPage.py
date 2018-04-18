#coding=utf-8
from util.get_by_local import GetByLocal

class DetailPage:
    '''获取发票详情页元素'''
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_invoiceDetail_element(self):
        """获取发票详情四个字"""
        return self.getByLocal.get_element('detail_element','invoiceDetail')

    def get_previewDownload_element(self):
        """获取预览下载四个字"""
        return self.getByLocal.get_element('detail_element','previewDownload')

    def get_reimbursement_element(self):
        """获取报销两个字"""
        return self.getByLocal.get_element('detail_element', 'reimbButton')

    def get_invoiceCheck_element(self):
        """获取发票查验四个字"""
        return self.getByLocal.get_element('detail_element', 'invoiceCheck')

    def get_tobaccoButton_element(self):
        """获取烟酒按钮"""
        return self.getByLocal.get_element('detail_element','tobaccoButton')

    def get_peservationButton_element(self):
        """获取保存按钮"""
        return self.getByLocal.get_element('detail_element','peservationButton')

    def get_sendEmail_element(self):
        """获取打印发票按钮"""
        return self.getByLocal.get_element('detail_element', 'sendEmail')

    def get_emailEidtText_element(self):
        """获取邮箱发送输入框"""
        return self.getByLocal.get_element('detail_element','emailEidtText')

    def get_print_element(self):
        """获取打印两个字"""
        return self.getByLocal.get_element('detail_element', 'print_')

    def get_checkPageText_element(self):
        """获取查验页面提示"""
        return self.getByLocal.get_element('detail_element', 'checkPageText')

    def get_remarks_element(self):
        """获取备注说明按钮"""
        return self.getByLocal.get_element('detail_element', 'remarks')

    def get_remarksEidx_element(self):
        """获取备注输入框"""
        return self.getByLocal.get_element('detail_element', 'remarksEidx')

    def get_peservation_element(self):
        """获取保存按钮"""
        return self.getByLocal.get_element('detail_element', 'peservation')

    def get_customer_element(self):
        """获取自定义按钮"""
        return self.getByLocal.get_element('detail_element', 'customer')

    def get_customerEidx_element(self):
        """获取自定义待办输入框"""
        return self.getByLocal.get_element('detail_element', 'customerEidx')

    def get_deleteText_element(self):
        """获取删除文本"""
        return self.getByLocal.get_element('detail_element', 'deleteText')

    def get_deleteButton_element(self):
        """获取删除按钮"""
        return self.getByLocal.get_element('detail_element', 'deleteButton')

    def get_reminding_element(self):
        """获取是否提醒"""
        return self.getByLocal.get_element('detail_element', 'reminding')

    def get_dateEidex_element(self):
        """获取时间控件输入框"""
        return self.getByLocal.get_element('detail_element', 'dateEidex')

    def get_quxiaoText_element(self):
        """获取取消按钮"""
        return self.getByLocal.get_element('detail_element', 'quxiaoText')


    def back(self):
        """返回"""
        self.driver.back()