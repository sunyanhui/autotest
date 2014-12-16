#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from action.pagefactory import PageFactory
from common import config
import unittest
import time

from testdata.osms.data_supermarket_manager import *

class TestSupermarketManager(unittest.TestCase):
    u'''
    测试超市修改角色
    '''
    def setUp(self):
        self.login = PageFactory.creat_po('login')
        self.supermarket_manager = PageFactory.creat_po('supermarket_manager')

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_modify_manager_case1(self):
        u'''测试超市添加操作员'''
        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_manager_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_manager.add_manager(**test_modify_manager_case1)
        self.assertTrue(r['result'], r['msg'])

    def test_modify_manager_case2(self):
        u'''测试超市删除操作员'''
        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_manager_case2)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_manager.del_manager(**test_modify_manager_case2)
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketManager))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()