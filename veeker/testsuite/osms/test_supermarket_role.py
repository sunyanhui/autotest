#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from action.pagefactory import PageFactory
from common import config
import unittest
import time

from testdata.osms.data_supermarket_role import *

class TestSupermarketRole(unittest.TestCase):
    u'''
    测试超市修改角色
    '''
    def setUp(self):
        self.login = PageFactory.creat_po('login')
        self.supermarket_role = PageFactory.creat_po('supermarket_role')

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_modify_role_case1(self):
        u'''测试超市添加角色'''
        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_role_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_role.add_role(**test_modify_role_case1)
        self.assertTrue(r['result'], r['msg'])

    def test_modify_role_case2(self):
        u'''测试超市删除角色'''
        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_role_case2)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_role.del_role(**test_modify_role_case2)
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketRole))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()