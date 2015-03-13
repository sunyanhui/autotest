#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.person.data_person_modify_password import *
from action.action_login import Login
from action.person.action_person_modify_password import PersonModifyPassword

import unittest
import logging
import time

class TestPersonModifyPassword(unittest.TestCase):
    u'''
    测试个人修改密码
    '''
    def setUp(self):
        self.login_page = Login()
        self.modify_password_page = PersonModifyPassword()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_password_case1(self):
        u'''测试个人修改密码功能'''

        # 打开首页，并登录
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_password_case1_1)
        self.assertTrue(r.result, r.msg)

        # 修改密码
        r = self.modify_password_page.modify_password(**test_modify_password_case1_1)
        self.assertTrue(r.result, r.msg)

        # 使用修改后的密码登录
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_password_case1_2)
        self.assertTrue(r.result, r.msg)

        # 把密码修改回来
        r = self.modify_password_page.modify_password(**test_modify_password_case1_2)
        self.assertTrue(r.result, r.msg)