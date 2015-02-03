#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_modify_password import *
from action.action_login import Login
from action.enterprise.action_enterprise_modify_password import EnterpriseModifyPassword
import unittest
import logging
import time

class TestEnterpriseModifyPassword(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login = Login()
        self.enterprise_modify_password = EnterpriseModifyPassword()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_modify_password_case1(self):
        u'''测试超市修改密码功能'''
        self.assertTrue(self.login.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login.login(**test_modify_password_case1)
        self.assertTrue(r.result, r.msg)
        r = self.enterprise_modify_password.modify_pass(**test_modify_password_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_password_case2(self):
        u'''测试超市修改密码功能，把密码修改回来'''
        self.assertTrue(self.login.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login.login(**test_modify_password_case2)
        self.assertTrue(r.result, r.msg)
        r = self.enterprise_modify_password.modify_pass(**test_modify_password_case2)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseModifyPassword))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()