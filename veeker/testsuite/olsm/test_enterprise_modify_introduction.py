#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_modify_introduction import *
from action.action_login import Login
from action.enterprise.action_enterprise_introduction import EnterpriseIntroduction
import unittest
import time

class TestEnterpriseModifyIntroduction(unittest.TestCase):
    u'''
    测试企业修改企业介绍、企业文化、企业组织架构等
    '''
    def setUp(self):
        self.login_page = Login()
        self.modify_introduction_page = EnterpriseIntroduction()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()


    def test_modify_introduction_case1(self):
        u'''测试企业修改企业介绍内容'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case1)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_introduction(**test_modify_introduction_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_introduction_case2(self):
        u'''测试企业修改企业文化内容'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case2)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_culture(**test_modify_introduction_case2)
        self.assertTrue(r.result, r.msg)


    def test_modify_introduction_case3(self):
        u'''测试企业修改企业组织架构内容'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_introduction_case3)
        self.assertTrue(r.result, r.msg)
        r = self.modify_introduction_page.modify_structure(**test_modify_introduction_case3)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseModifyIntroduction))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()