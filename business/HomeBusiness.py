#coding=utf-8

from handle.HomeHandle import HomeHandle
import time

class HomeBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.home_handle = HomeHandle(driver)


    def get_plusIcon(self):
        """获取底部加号"""
        return self.home_handle.isdisplay_plusIcon()

    def enter_home(self):
        """进入首页"""
        self.home_handle.click_home()

    def enter_service(self):
        """进入服务页面"""
        self.home_handle.click_service()
        time.sleep(2)

    def enter_add_scan(self):
        """进入新增扫码页面"""
        time.sleep(2)
        self.home_handle.click_plusIcon()
        time.sleep(1)
        self.home_handle.click_addInvoice()

    def judge_has_Jurisdiction(self):
        """判断是否具有权限，如果没有则授予权限"""
        if self.home_handle.isdisplay_setPermission() == True:
            #如果获取到设置权限按钮,则点击设置权限按钮
            self.home_handle.click_setPermission()
            try:
                #底部弹框授予权限
                self.home_handle.click_alwaysAllow()
                try:
                    self.home_handle.click_iKnow()
                except:
                    pass
            except:
                #弹出页面授予权限
                self.home_handle.click_Jurisdiction()
                self.home_handle.click_permissionSwitch()

    def get_scanOneScan(self):
        """获取扫码页面扫一扫"""
        time.sleep(1)
        return self.home_handle.isdisplay_scanOneScan()

    # def album_distinguish_QRcode(self):
    #     """相册识别二维码"""
    #     path = r'D:\PycharmProjects\Appium27\img\2018-03-25-17_01_24.jpg'
    #     try:
    #         #self.home_handle.click_album()
    #         #self.judge_has_Jurisdiction()
    #         time.sleep(10)
    #         self.home_handle.send_album(path)
    #     except:
    #         self.home_handle.send_album(path)


    def enter_add_take_photo(self):
        """进入拍照页面"""
        self.home_handle.click_OCR()

    def enter_manualInput(self):
        """进入手动输入页面"""
        self.home_handle.click_manualInput()

    def weChatBag_add(self):
        """卡包归集"""
        time.sleep(2)
        self.home_handle.click_plusIcon()
        self.home_handle.click_weChatBag()
        time.sleep(3)
        self.home_handle.click_bagInvoiceId()
        self.home_handle.click_confirm()
        self.home_handle.get_toast('微信卡包数据拉取中')
