#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from common import config
from testdata.olsm.data_enterprise_manager import *
from action.pagefactory import PageFactory
import unittest
import time

class TestEnterpriseManager(unittest.TestCase):
    u'''
    测试超市修改角色
    '''
    def setUp(self):
        self.login_page = PageFactory.creat_po('login')
        self.manager_page = PageFactory.creat_po('enterprise_manager')

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_manager_case1(self):
        u'''测试企业添加操作员'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.add_manager(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_manager_case2(self):
        u'''测试企业删除操作员'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.del_manager(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseManager))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()