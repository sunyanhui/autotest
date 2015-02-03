#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_release_zhaoshang_information import *
from action.action_login import Login
from action.supermarket.action_supermarket_release_zhaoshang_information import SupermarketReleaseZhaoshangInformation
import unittest
import time

class TestSupermarketReleaseZhaoshangInformation(unittest.TestCase):
    u'''
    测试超市招商信息
    '''
    def setUp(self):
        self.login_page = Login()
        self.release_zhaoshang_information_page = SupermarketReleaseZhaoshangInformation()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_release_zhaoshang_information_case1(self):
        u'''测试超市添加招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.add()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case2(self):
        u'''测试超市修改招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.modify()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case3(self):
        u'''测试超市发布招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.release()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case4(self):
        u'''测试超市关闭招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.close()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case5(self):
        u'''测试超市删除招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.delete()
        self.assertTrue(r.result, r.msg)