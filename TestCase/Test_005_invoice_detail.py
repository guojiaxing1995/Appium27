#coding=utf-8
from TestCase import ParameTestCase
from business.ManualBusiness import ManualBusiness
from business.HomeBusiness import HomeBusiness
from business.DetailBusiness import DetailBusiness
from business.WalletBusiness import WalletBusiness
import sys,time

class InvoiceDetail(ParameTestCase):
    """
    发票详情
    """
    @classmethod
    def setUpClass(cls):
        cls.home_business = HomeBusiness(cls.driver)
        cls.manual_business = ManualBusiness(cls.driver)
        cls.wallet_business = WalletBusiness(cls.driver)
        cls.detail_business = DetailBusiness(cls.driver)

    def setUp(self):
        pass

    def test_001_enter_eInvoice(self):
        """进入电票详情页面"""
        self.home_business.enter_service()
        self.wallet_business.choose_eInvoice_enter()

    def test_002_eInvoice_print(self):
        """电票打印"""
        self.detail_business.enter_preview_download()
        self.detail_business.ele_invoice_print()

    def test_003_eInvoice_print(self):
        """电票发送邮箱"""
        self.detail_business.send_email()
        self.driver.back()

    def test_004_eInvoice_check(self):
        """电票查验"""
        self.detail_business.eleInvoice_check()

    def test_005_invoice_remarks(self):
        """发票备注"""
        self.detail_business.invoice_remarks()

    def test_006_new_customer(self):
        """新建自定义待办"""
        self.detail_business.customer_need_do()

    def test_007_remove_customer(self):
        """删除自定义待办"""
        self.detail_business.cusromer_delete()

    def test_008_eInvoice_jiyiji(self):
        """电票记一记"""
        self.detail_business.add_jiyiji()

    def test_009_delete_invoice(self):
        """详情页删除电票"""
        self.detail_business.delete_invoice()

    def test_010_enter_paper_invoice(self):
        """进入纸票详情"""
        self.wallet_business.eInvoice_choose_all()
        self.wallet_business.choose_paperInvoice_enter()

    def test_011_add_photo(self):
        """上传附件，未实现"""
        pass

    def test_012_download_photo(self):
        """下传附件，未实现"""
        pass

    def test_013_delete_photo(self):
        """删除附件，未实现"""
        pass

    def test_014_delete_invoice(self):
        """详情页删除纸票"""
        self.detail_business.delete_invoice()

    def test_015_enter_train(self):
        """进入火车票详情"""
        self.wallet_business.train_choose_all()
        self.wallet_business.choose_train_enter()

    def test_016_train_jiyiji(self):
        """火车票记一记"""
        self.detail_business.add_jiyiji()

    def test_017_delete_train(self):
        """详情页删除火车票"""
        self.detail_business.delete_invoice()

    def test_018_enter_taxi(self):
        """进入打车票详情"""
        self.wallet_business.taxi_choose_all()
        self.wallet_business.choose_taxi_enter()

    def test_019_delete_taxi(self):
        """详情页删除打车票"""
        self.detail_business.delete_invoice()


    def tearDown(self):
        if sys.exc_info()[0]:
            now = time.strftime('%Y-%m-%d-%H_%M_%S')
            self.driver.save_screenshot('../img/'+now+'.jpg')