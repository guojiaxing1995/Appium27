#coding=utf-8
from page.HomePage import HomePage
from page.LoginPage import LoginPage

class HomeHandle:
    def __init__(self,driver):
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)

    def isdisplay_plusIcon(self):
        """判断底部加号是否存在"""
        return self.home_page.get_plusIcon_element().is_displayed()

    def click_plusIcon(self):
        """点击底部加号"""
        self.home_page.get_plusIcon_element().click()

    def click_addInvoice(self):
        """点击新增票按钮"""
        self.home_page.get_addInvoice_element().click()

    def isdisplay_setPermission(self):
        """判断设置权限按钮是否存在"""
        return self.home_page.get_setPermission().is_displayed()

    def click_setPermission(self):
        """点击权限设置按钮"""
        self.home_page.get_setPermission().click()

    def click_alwaysAllow(self):
        """点击始终允许按钮"""
        self.home_page.get_alwaysAllow().click()

    def click_Jurisdiction(self):
        """点击设置里面的权限按钮"""
        self.home_page.get_Jurisdiction().click()

    def click_permissionSwitch(self):
        """点击应用权限里面的开放权限选择按钮"""
        elements = self.home_page.get_permissionSwitch()
        for switch in elements:
            switch.click()

    def click_iKnow(self):
        """点击我知道了"""
        self.home_page.get_iKnow().click()

    def isdisplay_scanOneScan(self):
        """判断扫一扫三个字是否存在"""
        return self.home_page.get_scanOneScan_element().is_displayed()

    def click_OCR(self):
        """点击ocr识别按钮"""
        self.home_page.get_OCR_element().click()

    def send_album(self,path):
        """点击相册按钮"""
        self.home_page.get_album_element().send_keys(path)

    def click_album(self):
        """点击相册按钮"""
        self.home_page.get_album_element().click()

    def click_manualInput(self):
        """点击手动输入按钮"""
        self.home_page.get_manualInput_element().click()

    def click_weChatBag(self):
        """点击微信卡包"""
        self.home_page.get_weChatBag_element().click()

    def click_bagInvoiceId(self):
        """点击微信卡包卡片选择框"""
        self.home_page.get_bagInvoiceId_element().click()

    def click_confirm(self):
        """点击微信卡包"""
        self.home_page.get_confirm_element().click()

    def click_service(self):
        """点击服务按钮"""
        self.home_page.get_service_element().click()

    def click_discover(self):
        """点击服务按钮"""
        self.home_page.get_discover_element().click()

    def click_home(self):
        """点击首页按钮"""
        self.home_page.get_home_element().click()

    def click_serachInvoice_edittext(self):
        """点击搜索发票输入框"""
        self.home_page.get_serachInvoice_element().click()

    def send_serachInvoice_edittext(self,text):
        """输入搜索发票框"""
        self.home_page.get_serachInvoice_element().send_keys(text)

    def get_toast(self,test):
        self.login_page.get_toast(test)


