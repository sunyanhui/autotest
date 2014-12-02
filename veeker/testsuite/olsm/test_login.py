#!/usr/bin/python2.7
#coding=utf-8

from testdata.data_login import *
from action.slogin import Login
import unittest
import logging
import time

class TestLogin(unittest.TestCase):
    u'''
    测试登录功能
    '''

    def setUp(self):
        self.login = Login()
        self.login.open_browser("http://www.wiki168.com")

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    #testcase1
    def test_login_case1(self):
        u'''测试企业正常登录'''
        r = self.login.login(**test_login_case1)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case1['title'], r['msg'])

    #testcase2
    def test_login_case2(self):
        u'''测试个人正常登录'''
        r = self.login.login(**test_login_case2)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case2['title'], u"登录成功，但身份不正确")

    #testcase3
    def test_login_case3(self):
        u'''测试市级分销商正常登录'''
        r = self.login.login(**test_login_case3)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case3['title'], u"登录成功，但身份不正确")

    #testcase4
    def test_login_case4(self):
        u'''测试分销商操作员正常登录'''
        r = self.login.login(**test_login_case4)
        self.assertEqual(r['title'], test_login_case4['title'], u"登录成功，但身份不正确")

    #testcase5
    def test_login_case5(self):
        u'''测试企业操作员正常登录'''
        r = self.login.login(**test_login_case5)
        self.assertEqual(r['title'], test_login_case5['title'], u"登录成功，但身份不正确")

    #testcase6
    def test_login_case6(self):
        u'''测试超市正常登录'''
        r = self.login.login(**test_login_case6)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case6['title'], u"登录成功，但身份不正确")

    #testcase7
    def test_login_case7(self):
        u'''测试联盟店正常登录'''
        r = self.login.login(**test_login_case7)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case7['title'], u"登录成功，但身份不正确")

    #testcase8
    def test_login_case8(self):
        u'''测试联盟店操作员正常登录'''
        r = self.login.login(**test_login_case8)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case8['title'], u"登录成功，但身份不正确")

    #testcase9
    def test_login_case9(self):
        u'''测试超市操作员正常登录'''
        r = self.login.login(**test_login_case9)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], test_login_case9['title'], u"登录成功，但身份不正确")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestLogin))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()
