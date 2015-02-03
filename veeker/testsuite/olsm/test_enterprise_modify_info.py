#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_modify_info import *
from action.action_login import Login
from action.enterprise.action_enterprise_modify_info import EnterpriseModifyInfo
import unittest
import logging
import time

class TestEnterpriseModifyInfo(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login = Login()
        self.enterpriseModifyInfo = EnterpriseModifyInfo()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_modify_info_case1(self):
        u'''测试超市版注册功能，注册成功后，使用新注册的账号登录'''
        self.assertTrue(self.login.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login.login(**test_modify_info_case1)
        self.assertTrue(r.result, r.msg)

        r = self.enterpriseModifyInfo.modify_info(**test_modify_info_case1)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseModifyInfo))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()