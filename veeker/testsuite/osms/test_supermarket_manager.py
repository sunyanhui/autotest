#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
if config.ENV == 'test':
    from testdata_test.osms.data_supermarket_manager import *
else:
    from testdata_online.osms.data_supermarket_manager import *
from action.pagefactory import PageFactory

import unittest
import time



class TestSupermarketManager(unittest.TestCase):
    u'''
    测试超市修改角色
    '''
    def setUp(self):
        self.login_page = PageFactory.creat_po('login')
        self.manager_page = PageFactory.creat_po('supermarket_manager')

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_manager_case1(self):
        u'''测试超市添加操作员'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.add_manager(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_manager_case2(self):
        u'''测试超市删除操作员'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.del_manager(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketManager))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()