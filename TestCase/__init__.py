import unittest
import sys,time
from base.BaseDriver import BaseDriver


class ParameTestCase(unittest.TestCase):
    """
    该类继承unittest  该类的子类可以传参数
    """
    def __init__(self,methodName='runTest',parames=None):
        super(ParameTestCase,self).__init__(methodName)
        global parame
        parame = parames

    @classmethod
    def get_driver(cls):
        """
        实例化driver
        :return:
        """
        baseDriver = BaseDriver()
        cls.driver = baseDriver.get_android_driver(parame)

    @classmethod
    def kill_driver(cls):
        cls.driver.quit()

    def setUp(self):
        self.imgs = []

    def tearDown(self):
        if sys.exc_info()[0]:
            now = time.strftime('%Y-%m-%d-%H_%M_%S')
            self.driver.save_screenshot('../img/'+now+'.jpg')
            #将截图加入报告
            self.imgs.append(self.driver.get_screenshot_as_base64())
