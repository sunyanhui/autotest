#!/usr/bin/python3.3
#coding=utf-8

import sys, os, unittest, time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selenium import webdriver
from testdata.dlogin import *
from script import slogin, sbrowser







class TestLogin(unittest.TestCase):

    def setUp(self):
        self.drive = sbrowser.Browser().openbrowser()

    #testcase1
    @unittest.skipIf(test_login_case1['tag']=='no',u'test_login+case1跳过测试')
    def test_login_case1(self):
        u'''测试登录成功'''

        u = test_login_case1['useraccount']
        p = test_login_case1['password']
        v = test_login_case1['vertifycode']
        r = test_login_case1['rememberusername']
        drive = self.drive

        loginresult = slogin.Login(drive).login_for_test(u, p, v, r)
        self.assertEqual(loginresult['vertifycodeprompt'],test_login_case1['vertifycodeprompt'],msg='login fail')


    #testcase2
    @unittest.skipIf(test_login_case2['tag']=='no',u'test_login_case2 跳过测试')
    def test_login_case2(self):
        u'''用户名输入为空'''

        u = test_login_case2['useraccount']
        p = test_login_case2['password']
        v = test_login_case2['vertifycode']
        r = test_login_case1['rememberusername']
        drive = self.drive

        loginresult = slogin.Login(drive).login_for_test(u, p, v, r)
        self.assertEqual(loginresult['result'], test_login_case2['result'], 'login successful')
        self.assertEqual(loginresult['usernameprompt'], test_login_case2['usernameprompt'], 'Usename Prompt Error')

    def tearDown(self):
        time.sleep(1)
        self.drive.quit()


if __name__ == '__main__':
    unittest.main()
