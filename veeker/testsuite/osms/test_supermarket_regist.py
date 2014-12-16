#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.data_regist import *
from action.action_login import Login
from action.action_regist import Regist
from common import config
import unittest
import logging
import time

class TestOsmsRegist(unittest.TestCase):
    u'''
    测试注册
    '''
    def setUp(self):
        self.login = Login()
        self.regist = Regist()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_regist_case1(self):
        u'''测试超市版注册功能，注册成功后，使用新注册的账号登录'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.regist.submit_information(**test_regist_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.regist.regist(**test_regist_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.login.login(**dict(username=r['useraccount'], password='888888', ifrememberusername='yes'))
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOsmsRegist))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()