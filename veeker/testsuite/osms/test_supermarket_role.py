#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_role import *
from action.pagefactory import PageFactory
import unittest
import time

class TestSupermarketRole(unittest.TestCase):
    u'''
    测试超市修改角色
    '''
    def setUp(self):
        self.login_page = PageFactory.creat_po('login')
        self.role_page = PageFactory.creat_po('supermarket_role')

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_role_case1(self):
        u'''测试超市添加角色'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_role_case1)
        self.assertTrue(r.result, r.msg)

        r = self.role_page.add_role(**test_modify_role_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_role_case2(self):
        u'''测试超市删除角色'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_role_case2)
        self.assertTrue(r.result, r.msg)

        r = self.role_page.del_role(**test_modify_role_case2)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketRole))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()