#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_modify_introduction import *
from action.action_login import Login
from action.supermarket.action_supermarket_introduction import SupermarketIntroduction
import unittest
import time

class TestSupermarketModifyIntroduction(unittest.TestCase):
    u'''
    测试超市修改超市介绍、文化、组织架构等
    '''
    def setUp(self):
        self.login_page = Login()
        self.modify_introduction_page = SupermarketIntroduction()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()


    def test_modify_introduction_case1(self):
        u'''测试超市修改超市介绍内容'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case1)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_introduction(**test_modify_introduction_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_introduction_case2(self):
        u'''测试超市修改超市文化内容'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case2)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_culture(**test_modify_introduction_case2)
        self.assertTrue(r.result, r.msg)


    def test_modify_introduction_case3(self):
        u'''测试超市修改超市组织架构内容'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case3)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_structure(**test_modify_introduction_case3)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketModifyIntroduction))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()