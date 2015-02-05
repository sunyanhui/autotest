#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_shop_role import *
from action.action_login import Login
from action.shop.action_shop_role import ShopRole
import unittest
import time


class TestShopRole(unittest.TestCase):
    u"""
    测试联盟店修改角色
    """

    def setUp(self):
        self.login_page = Login()
        self.role_page = ShopRole()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_role_case1(self):
        u"""测试联盟店添加角色"""
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        r = self.login_page.login(**test_modify_role_case1)
        self.assertTrue(r.result, r.msg)

        r = self.role_page.add_role(**test_modify_role_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_role_case2(self):
        u"""测试联盟店删除角色"""
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        r = self.login_page.login(**test_modify_role_case2)
        self.assertTrue(r.result, r.msg)

        r = self.role_page.del_role(**test_modify_role_case2)
        self.assertTrue(r.result, r.msg)