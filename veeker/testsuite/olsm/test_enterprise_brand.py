#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_brand import *
from action.action_login import Login
from action.enterprise.action_enterprise_goods_brand import EnterpriseGoodsBrand
import unittest
import time

class TestEnterpriseBrand(unittest.TestCase):
    u'''
    测试企业商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.brand_page = EnterpriseGoodsBrand()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_brand_case1(self):
        u'''测试企业添加商品品牌，然后删除'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_brand_case1)
        self.assertTrue(r.result, r.msg)

        r = self.brand_page.add_brand()
        self.assertTrue(r.result, r.msg)
        brand_name = r.brand_name

        r = self.brand_page.del_brand(brand_name)
        self.assertTrue(r.result, r.msg)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseBrand))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()