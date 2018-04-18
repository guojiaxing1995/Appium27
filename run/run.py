#coding=utf-8
import unittest,time,HTMLTestRunnerCN
from util.server import Server
from util.OperateYaml import OperateYaml
import multiprocessing
from TestCase.Test_001_login import Login
from TestCase.Test_002_invoice_collection import InvoiceCollection

class Run:
    def __init__(self):
        server = Server()
        server.main()
        time.sleep(20)
        operaterYaml = OperateYaml()
        self.deivces_num = operaterYaml.get_cloumn()

    def creatsuit(self,i):
        test_suite = unittest.TestSuite()
        # # 测试文件查找的目录
        # test_dir = '../TestCase'
        # # discover方法筛选Test开头的文件
        # discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*.py', top_level_dir=None)
        # # 将筛选出来的用例,循环添加套件
        # for test_class in discover:
        #     for test_case in test_class:

        #         test_suite.addTest(test_class(test_case,parame=i))
        test_suite.addTest(Login("test_001_slide_carouselfigure",parames=i))
        test_suite.addTest(Login("test_002_phone_num_login", parames=i))
        # test_suite.addTest(InvoiceCollection("test_001_enter_add_scan", parames=i))
        # test_suite.addTest(InvoiceCollection("test_002_enter_manualInput", parames=i))
        # test_suite.addTest(InvoiceCollection("test_003_manual_add_invoice", parames=i))
        # test_suite.addTest(InvoiceCollection("test_004_enter_addTrain", parames=i))
        # test_suite.addTest(InvoiceCollection("test_005_manual_add_train", parames=i))
        # test_suite.addTest(InvoiceCollection("test_006_enter_addTiax", parames=i))
        # test_suite.addTest(InvoiceCollection("test_007_manual_add_taxi", parames=i))
        #test_suite.addTest(InvoiceCollection("test_008_wallet_delete_invoice", parames=i))
        # test_suite.addTest(InvoiceCollection("test_009_enter_manaualCheck", parames=i))
        # test_suite.addTest(InvoiceCollection("test_010_manaualCheck", parames=i))
        # test_suite.addTest(InvoiceCollection("test_011_weChatBag_add", parames=i))

        return test_suite

    def run_case_creat_report(self,i,title=u'Appium自动化',description=u'用例执行情况:',tester=u'自动化测试团队'):
        # 获取当前时间
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 定义报告存放路径,确保此路径已存在
        filename = '../report/' + now + 'result.html'
        fp = open(filename, 'wb')
        # 设定测试报告相关信息
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title=title,
            description=description,
            tester=tester
        )

        runner.run(self.creatsuit(i))
        # 关闭报告文件
        fp.close()

    def run(self):
        """
        多进程运行case
        """
        threads = []
        for i in range(int(self.deivces_num)):
            t = multiprocessing.Process(target=self.run_case_creat_report, args=(i,))
            threads.append(t)
        for j in threads:
            j.start()

if __name__=='__main__':
    run = Run()
    run.run()
