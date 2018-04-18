#coding=utf-8
import unittest

class ParameTestCase(unittest.TestCase):
    """
    该类继承unittest  该类的子类可以传参数
    """
    def __init__(self,methodName='runTest',para=None):
        super(ParameTestCase,self).__init__(methodName)
        global parame
        parame = para