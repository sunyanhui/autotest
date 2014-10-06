#!/usr/bin/python2.7
#coding=utf-8

from testdata.dlogin import *
from script.slogin import Login
from script.sbrowser import Browser
import unittest
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().openbrowser

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    #testcase1
    @unittest.skipIf(test_login_case1['tag']=='no', u"skip test_login_case1")
    def test_login_case1(self):
        u'''测试个人用户登录成功'''
        driver = self.driver
        r = Login(driver).login(**test_login_case1)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], u'个人中心首页', r['msg'])

    #testcase2
    @unittest.skipIf(test_login_case2['tag']=='no', u"skip test_login_case2")
    def test_login_case2(self):
        u'''测试分销商登录成功'''
        driver = self.driver
        r = Login(driver).login(**test_login_case2)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], u'分销商系统', r['msg'])

    #testcase3
    @unittest.skipIf(test_login_case3['tag']=='no', u"skip test_login_case3")
    def test_login_case3(self):
        u'''测试企业登录成功'''
        driver = self.driver
        r = Login(driver).login(**test_login_case3)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(r['title'], u'sun|管理平台', r['msg'])

    #testcase4
    @unittest.skipIf(test_login_case4['tag']=='no', u"skip test_login_case4")
    def test_login_case4(self):
        u'''用户名输入为空'''
        driver = self.driver
        r = Login(driver).login(**test_login_case4)
        self.assertFalse(r['result'], r['msg'])

    #testcase5
    @unittest.skipIf(test_login_case5['tag']=='no', u"skip test_login_case5")
    def test_login_case5(self):
        u'''用户名输入错误'''
        driver = self.driver
        r = Login(driver).login(**test_login_case5)
        self.assertFalse(r['result'], r['msg'])

    #testcase6
    @unittest.skipIf(test_login_case6['tag']=='no', u"skip test_login_case6")
    def test_login_case6(self):
        u'''用户名输入在正确的基础上多1位'''
        driver = self.driver
        r = Login(driver).login(**test_login_case6)
        self.assertFalse(r['result'], r['msg'])

    #testcase7
    @unittest.skipIf(test_login_case7['tag']=='no', u"skip test_login_case7")
    def test_login_case7(self):
        u'''密码输入错误'''
        driver = self.driver
        r = Login(driver).login(**test_login_case7)
        self.assertFalse(r['result'], r['msg'])

    #testcase8
    @unittest.skipIf(test_login_case8['tag']=='no', u"skip test_login_case8")
    def test_login_case8(self):
        u'''密码输入为空'''
        driver = self.driver
        r = Login(driver).login(**test_login_case8)
        self.assertFalse(r['result'], r['msg'])

    #testcase9
    @unittest.skipIf(test_login_case9['tag']=='no', u"skip test_login_case9")
    def test_login_case9(self):
        u'''验证码输入为空'''
        driver = self.driver
        r = Login(driver).login(**test_login_case9)
        self.assertFalse(r['result'], r['msg'])

if __name__ == '__main__':

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestLogin))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()
