#!/usr/bin/python2.7
#coding=utf-8

import sys
import os
import unittest
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selenium import webdriver
from testdata.dlogin import *
from script import slogin, sbrowser

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.drive = sbrowser.Browser().openbrowser()

    def tearDown(self):
        time.sleep(1)
        self.drive.quit()

    def mode(func):
        def mode1(self):
            u'''测试登录成功'''
            a = func(self)
            u = a['useraccount']
            p = a['password']
            v = a['vertifycode']
            r = a['rememberusername']
            drive = self.drive

            loginresult = slogin.Login(drive).login(u, p, v, r)
            self.assertEqual(loginresult['result'],a['result'],
                             msg=loginresult['describtion']+'  '+loginresult['errorimg'])
        return mode1


    #@mode
    #@unittest.skipIf(test_login_case1['tag']=='no', u"skip test_login_case1")
    #def test_login_case1(self):
    #    return test_login_case2



    #@mode
    #@unittest.skipIf(test_login_case2['tag']=='no',u'skip test_login_case2')
    #def test_login_case2(self):
    #    return test_login_case2

    #testcase1
    #@unittest.skipIf(test_login_case1['tag']=='no', u"skip test_login_case1")
    def test_login_case1(self):
        u'''测试登录成功'''

        u = test_login_case1['useraccount']
        p = test_login_case1['password']
        v = test_login_case1['vertifycode']
        r = test_login_case1['rememberusername']
        drive = self.drive

        loginresult = slogin.Login(drive).login(u, p, v, r)
        self.assertEqual(loginresult['result'],test_login_case1['result'],
                         msg=loginresult['describtion']+'  '+loginresult['errorimg'])


    #testcase2
    def test_login_case2(self):
        u'''用户名输入为空'''

        u = test_login_case2['useraccount']
        p = test_login_case2['password']
        v = test_login_case2['vertifycode']
        r = test_login_case1['rememberusername']
        drive = self.drive

        loginresult = slogin.Login(drive).login(u, p, v, r)
        self.assertEqual(loginresult['result'],test_login_case2['result'],
                         msg=loginresult['describtion']+'  '+loginresult['errorimg'])


if __name__ == '__main__':
    unittest.main()
