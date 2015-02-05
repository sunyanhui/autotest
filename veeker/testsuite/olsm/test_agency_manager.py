#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from common import config
from testdata.olsm.data_agency_manager import *
from action.action_login import Login
from action.agency.action_agency_manager import AgencyManager
import unittest
import time


class TestAgencyManager(unittest.TestCase):
    u"""
    测试分销商修改角色
    """

    def setUp(self):
        self.login_page = Login()
        self.manager_page = AgencyManager()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_manager_case1(self):
        u"""测试分销商添加操作员"""
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.add_manager(**test_modify_manager_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_manager_case2(self):
        u"""测试分销商删除操作员"""
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        r = self.login_page.login(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)

        r = self.manager_page.del_manager(**test_modify_manager_case2)
        self.assertTrue(r.result, r.msg)