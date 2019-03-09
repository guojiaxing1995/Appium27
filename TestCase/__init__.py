import unittest

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