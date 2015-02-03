#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_shop_basic_information import *
from action.action_login import Login
from action.shop.action_shop_basic_information import ShopBasicInformation
import unittest
import time

class TestShopBasicInformation(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.basic_information_page = ShopBasicInformation()

    def tearDown(self):
        pass
        #time.sleep(1)
        #self.login_page.quit()

    def test_basic_information_case1(self):
        u'''验证手机号输入10位数字'''

        case = test_shop_basic_information_case1
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case2(self):
        u'''验证手机号输入12位数字'''

        case = test_shop_basic_information_case2
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case3(self):
        u'''验证手机号输入为空'''

        case = test_shop_basic_information_case3
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case4(self):
        u'''验证手机号输入汉字'''

        case = test_shop_basic_information_case4
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case5(self):
        u'''验证手机号输入英文'''

        case = test_shop_basic_information_case5
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case6(self):
        u'''验证微信号输入特殊字符'''

        case = test_shop_basic_information_case6
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case7(self):
        u'''验证微信号输入空格'''

        case = test_shop_basic_information_case7
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertFalse(r.result, r.msg)


    def test_basic_information_case8(self):
        u'''验证微信号输入汉字'''

        case = test_shop_basic_information_case8
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case9(self):
        u'''验证微信号输入含字母、数字、下划线和减号的字符'''

        case = test_shop_basic_information_case9
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertFalse(r.result, r.msg)


    def test_basic_information_case10(self):
        u'''验证微信号输入小于5位的字符'''

        case = test_shop_basic_information_case10
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case11(self):
        u'''验证微信号输入大于20位的字符'''

        case = test_shop_basic_information_case11
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case12(self):
        u'''验证微信号输入5~20位的字符'''

        case = test_shop_basic_information_case12
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertFalse(r.result, r.msg)

    def test_basic_information_case13(self):
        u'''验证微信号输入为空'''

        case = test_shop_basic_information_case13
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertFalse(r.result, r.msg)


    def test_basic_information_case14(self):
        u'''验证微信号输入html字符'''

        case = test_shop_basic_information_case14
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_weixin(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case15(self):
        u'''验证开户行下拉框数据'''

        case = test_shop_basic_information_case15
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_bank_data(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.bank_list, case.bank_list)

    def test_basic_information_case16(self):
        u'''验证开户行所在地输入小于50个汉字'''

        case = test_shop_basic_information_case16
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_location(**case)
        self.assertFalse(r.result, r.msg)


    def test_basic_information_case17(self):
        u'''验证开户行所在地输入大于50个汉字'''

        case = test_shop_basic_information_case17
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_location(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case18(self):
        u'''验证开户行所在地输入字母、数字、空格、汉字、特殊字符'''

        case = test_shop_basic_information_case18
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_location(**case)
        self.assertFalse(r.result, r.msg)


    def test_basic_information_case19(self):
        u'''验证开户行输入为空'''

        case = test_shop_basic_information_case19
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_location(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case20(self):
        u'''验证对公账号输入框输入小于16个数字'''

        case = test_shop_basic_information_case20
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_agency_account(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case21(self):
        u'''验证对公账号输入框输入大于19个数字'''

        case = test_shop_basic_information_case21
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_agency_account(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case22(self):
        u'''验证对公账号输入框输入非数字的其它字符'''

        case = test_shop_basic_information_case22
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_agency_account(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case23(self):
        u'''对公账号输入框输入为空'''

        case = test_shop_basic_information_case23
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_agency_account(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)


    def test_basic_information_case24(self):
        u'''对公账号输入框粘贴进去有空格的数字'''

        case = test_shop_basic_information_case24
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_agency_account(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)

    def test_basic_information_case25(self):
        u'''验证正确保存基本信息'''

        case = test_shop_basic_information_case25
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.modify()
        self.assertTrue(r.result, r.msg)
