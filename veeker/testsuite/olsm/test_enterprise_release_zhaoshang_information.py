#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_release_zhaoshang_information import *
from action.action_login import Login
from action.enterprise.action_enterprise_release_zhaoshang_information import EnterpriseReleaseZhaoshangInformation
import unittest
import time

class TestEnterpriseReleaseZhaoshangInformation(unittest.TestCase):
    u'''
    测试企业招商信息
    '''
    def setUp(self):
        self.login_page = Login()
        self.release_zhaoshang_information_page = EnterpriseReleaseZhaoshangInformation()

    # def tearDown(self):
    #     time.sleep(1)
    #     self.login_page.quit()

    def test_release_zhaoshang_information_case1(self):
        u'''测试企业添加招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.add()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case2(self):
        u'''测试企业修改招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.modify()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case3(self):
        u'''测试企业发布招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.release()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case4(self):
        u'''测试企业关闭招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.close()
        self.assertTrue(r.result, r.msg)

    def test_release_zhaoshang_information_case5(self):
        u'''测试企业删除招商信息'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        r = self.login_page.login(**test_release_zhaoshang_information_case1)
        self.assertTrue(r.result, r.msg)

        r = self.release_zhaoshang_information_page.delete()
        self.assertTrue(r.result, r.msg)