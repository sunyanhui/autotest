#!/usr/bin/python2.7
#coding=utf-8

import sys
import os
import unittest
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from testdata.dlogin import *
from script import slogin, sbrowser

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = sbrowser.Browser().openbrowser

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    #testcase1
    @unittest.skipIf(test_login_case1['tag']=='no', u"skip test_login_case1")
    def test_login_case1(self):
        u'''测试登录成功'''
        driver = self.driver
        loginresult = slogin.Login(driver).login(**test_login_case1)
        self.assertEqual(loginresult['result'], True, msg=loginresult['msg']+'\n'+loginresult['img'])

    #testcase2
    @unittest.skipIf(test_login_case2['tag']=='no', u"skip test_login_case2")
    def test_login_case2(self):
        u'''测试登录成功'''
        driver = self.driver
        loginresult = slogin.Login(driver).login(**test_login_case2)
        self.assertEqual(loginresult['result'], False, msg=loginresult['msg']+'\n'+loginresult['img'])

    #testcase3
    @unittest.skipIf(test_login_case3['tag']=='no', u"skip test_login_case3")
    def test_login_case3(self):
        u'''测试登录成功'''
        driver = self.driver
        loginresult = slogin.Login(driver).login(**test_login_case3)
        self.assertEqual(loginresult['result'], False, msg=loginresult['msg']+'\n'+loginresult['img'])

if __name__ == '__main__':
    unittest.main()
