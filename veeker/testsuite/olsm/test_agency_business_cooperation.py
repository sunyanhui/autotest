#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_agency_business_cooperation import *
from action.action_login import Login
from action.agency.action_agency_business_cooperation import AgencyBusinessCooperation
import unittest
import time


class TestAgencyBusinessCooperation(unittest.TestCase):
    """测试分销商合作商家"""


    def setUp(self):
        self.login_page = Login()
        self.agency_business_cooperation_page = AgencyBusinessCooperation()

    # def tearDown(self):
    #     time.sleep(1)
    #     self.login_page.quit()

    def test_business_cooperation_case1(self):
        u"""测试合作商家页面-联盟状态下拉框列表数据"""

        case = test_agency_business_cooperation_case1
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #获取下拉框数据
        r = self.agency_business_cooperation_page.test_alliance_status()
        self.assertTrue(r.result, r.msg)
        self.assertEqual(r.alliance_status_list, case.alliance_status_list, u"联盟状态下拉列表数据错误")


    def test_business_cooperation_case2(self):
        u"""测试合作商家页面-商家搜索(正确数据)"""

        case = test_agency_business_cooperation_case2
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #获取下拉框数据
        r = self.agency_business_cooperation_page.search(**case)
        self.assertTrue(r.result, r.msg)


    def test_business_cooperation_case3(self):
        u"""测试合作商家页面-商家搜索(错误数据)"""

        case = test_agency_business_cooperation_case3
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #获取下拉框数据
        r = self.agency_business_cooperation_page.search(**case)
        self.assertFalse(r.result, r.msg)