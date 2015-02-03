#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_recruit import *
from action.action_login import Login
from action.supermarket.action_supermarket_recruit import SupermarketRecruit
import unittest
import time

class TestSupermarketRecruit(unittest.TestCase):
    u'''
    测试超市招聘信息
    '''
    def setUp(self):
        self.login_page = Login()
        self.recruit_page = SupermarketRecruit()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_recruit_case1(self):
        u'''测试超市添加招聘信息并删除'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_recruit_case1)
        self.assertTrue(r.result, r.msg)

        r = self.recruit_page.add_recruit()
        self.assertTrue(r.result, r.msg)
        position_name = r.position_name

        r = self.recruit_page.del_recruit(position_name)
        self.assertTrue(r.result, r.msg)