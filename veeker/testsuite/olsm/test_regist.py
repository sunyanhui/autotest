#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.data_regist import *
from action.action_login import Login
from action.action_regist import Regist
from common import config
import unittest
import logging
import time

class TestRegist(unittest.TestCase):
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
        u'''测试全国版注册页面，是否可收到验证码'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r1 = self.regist.submit_information(**test_regist_case1)
        self.assertTrue(r1['result'], r1['msg'])
        r2 = self.regist.regist(**test_regist_case1)
        self.assertTrue(r2['result'], r2['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestRegist))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()