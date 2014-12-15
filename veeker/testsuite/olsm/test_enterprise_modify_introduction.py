#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.olsm.data_enterprise_modify_introduction import *
from action.action_login import Login
from action.enterprise.action_enterprise_introduction import EnterpriseIntroduction
from common import config
import unittest
import logging
import time

class TestEnterpriseModifyIntroduction(unittest.TestCase):
    u'''
    测试企业修改企业介绍、企业文化、企业组织架构等
    '''
    def setUp(self):
        self.login = Login()
        self.enterprise_modify_introduction = EnterpriseIntroduction()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_modify_introduction_case1(self):
        u'''测试企业修改企业介绍内容'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_introduction_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.enterprise_modify_introduction.modify_introduction(**test_modify_introduction_case1)
        self.assertTrue(r['result'], r['msg'])

    def test_modify_introduction_case2(self):
        u'''测试企业修改企业文化内容'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_introduction_case2)
        self.assertTrue(r['result'], r['msg'])
        r = self.enterprise_modify_introduction.modify_culture(**test_modify_introduction_case2)
        self.assertTrue(r['result'], r['msg'])


    def test_modify_introduction_case3(self):
        u'''测试企业修改企业组织架构内容'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_introduction_case3)
        self.assertTrue(r['result'], r['msg'])
        r = self.enterprise_modify_introduction.modify_structure(**test_modify_introduction_case3)
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseModifyIntroduction))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()