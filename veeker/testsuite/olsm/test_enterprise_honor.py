#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_honor import *
from action.action_login import Login
from action.enterprise.action_enterprise_honor import EnterpriseHonor
import unittest
import time

class TestEnterpriseHonor(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.honor_page = EnterpriseHonor()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_honor_case1(self):
        u'''测试超市添加企业荣誉并删除'''
        self.assertTrue(self.login_page.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_honor_case1)
        self.assertTrue(r.result, r.msg)

        r = self.honor_page.add_honor()
        self.assertTrue(r.result, r.msg)
        honor_describe = r.describe

        r = self.honor_page.del_honor(honor_describe)
        self.assertTrue(r.result, r.msg)