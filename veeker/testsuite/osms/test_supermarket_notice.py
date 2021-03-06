#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_notice import *
from action.action_login import Login
from action.supermarket.action_supermarket_notice import SupermarketNotice
import unittest
import time

class TestSupermarketNotice(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.notice_page = SupermarketNotice()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_notice_case1(self):
        u'''测试超市添加通知公告并删除'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_notice_case1)
        self.assertTrue(r.result, r.msg)

        r = self.notice_page.add_notice()
        self.assertTrue(r.result, r.msg)
        title = r.title

        r = self.notice_page.del_notice(title)
        self.assertTrue(r.result, r.msg)