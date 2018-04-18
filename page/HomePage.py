#coding=utf-8
from util.get_by_local import GetByLocal
from base.PublicMethod import PublicMethod

class HomePage:
    '''获取首页元素'''
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_plusIcon_element(self):
        '''获取首页底部加号'''
        return self.getByLocal.get_element('home_element','plusIcon')

    def get_addInvoice_element(self):
        """获取新增票元素"""
        return self.getByLocal.get_element('home_element','addInvoice')

    def get_setPermission(self):
        """获取权限设置按钮"""
        return self.getByLocal.get_element('home_element','setPermission')

    def get_alwaysAllow(self):
        """获取始终允许按钮"""
        return self.getByLocal.get_element('home_element','alwaysAllow')

    def get_Jurisdiction(self):
        """获取设置里的权限按钮"""
        return self.getByLocal.get_element('home_element','Jurisdiction')

    def get_iKnow(self):
        """获取我知道了四个字"""
        return self.getByLocal.get_element('home_element','iKnow')

    def get_permissionSwitch(self):
        """获取设置页面所有权限选择框"""
        return self.getByLocal.get_element('home_element','permissionSwitch')

    def get_scanOneScan_element(self):
        """获取扫码页面扫一扫"""
        return self.getByLocal.get_element('home_element','scanOneScan')

    def get_album_element(self):
        """获取相册按钮"""
        return self.getByLocal.get_element('home_element','album')

    def get_OCR_element(self):
        """获取ocr识别按钮"""
        return self.getByLocal.get_element('home_element','OCR')

    def get_manualInput_element(self):
        """获取手动输入按钮"""
        return self.getByLocal.get_element('home_element','manualInput')

    def get_weChatBag_element(self):
        """获取微信卡包四个字"""
        return self.getByLocal.get_element('home_element','weChatBag')

    def get_bagInvoiceId_element(self):
        """获取微信卡包中的发票选择框"""
        return self.getByLocal.get_element('home_element','bagInvoiceId')

    def get_confirm_element(self):
        """获取确认按钮"""
        return self.getByLocal.get_element('home_element','confirm')

    def get_service_element(self):
        """获取服务按钮"""
        return self.getByLocal.get_element('home_element','service')

    def get_home_element(self):
        """获取首页按钮"""
        return self.getByLocal.get_element('home_element','home')

    def get_serachInvoice_element(self):
        """获取搜索发票输入框"""
        return self.getByLocal.get_element('home_element','serachInvoice')


