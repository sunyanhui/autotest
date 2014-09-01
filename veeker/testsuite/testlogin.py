#!/usr/bin/python3.3
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import sys, unittest, time, re
sys.path.append(r'D:\autotest\veeker')
from testdata import dlogin
from objectrepository.person import omycenter
from script import slogin, sbrowser




class TestLogin(unittest.TestCase):

    def setUp(self):
        self.drive = sbrowser.Browser().openbrowser()

    def test_login_case1(self):

        useraccount = dlogin.test_login_case1['useraccount']
        password = dlogin.test_login_case1['password']
        vertifycode = dlogin.test_login_case1['vertifycode']
        drive = self.drive

        logininstance = slogin.Login(drive)
        logininstance.login(useraccount, password, vertifycode)
        drive.implicitly_wait(30)
        #time.sleep(3)

        #drive.window_handles

        #drive.switch_to_window(a[0])

        #print drive.current_url
        #print drive.title.encode('utf-8')
        #print drive.page_source

        drive.find_element_by_link_text(u'密码修改').click()
        time.sleep(1)


    def test_login_case2(self):

        useraccount = dlogin.test_login_case2['useraccount']
        password = dlogin.test_login_case2['password']
        vertifycode = dlogin.test_login_case2['vertifycode']
        drive = self.drive

        logininstance = slogin.Login(drive)
        logininstance.login(useraccount, password, vertifycode)
        drive.implicitly_wait(30)
        print drive.current_url
        print drive.title.encode('utf-8')
        drive.find_element_by_link_text(u'退出登录').click()
        time.sleep(5)

    def tearDown(self):
        time.sleep(3)
        self.drive.quit()


if __name__ == '__main__':
    unittest.main()
