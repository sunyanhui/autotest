#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_shop_returns import *
from action.action_login import Login
from action.supermarket.action_supermarket_mall_homepage import MallHomePage
from action.shop.action_shop_customer_order_settlement import ShopCustomerOrderSettlement
from action.person.action_person_place_order import PlaceOrder
from action.person.action_person_goods_bought import GoodsBought
from action.shop.action_shop_approval_return import ShopApprovalReturn
import unittest
import time

class TestShopReturns(unittest.TestCase):
    u'''
    测试联盟店退货流程
    '''
    def setUp(self):
        self.login_page = Login()
        self.mall_page = MallHomePage()
        self.place_order_page = PlaceOrder()
        self.order_settlement_page = ShopCustomerOrderSettlement()
        self.goods_bought = GoodsBought()
        self.approval_return_page = ShopApprovalReturn()

    def tearDown(self):

        time.sleep(1)
        self.login_page.quit()

    def test_returns_case1(self):
        u'''测试正常退货流程'''

        # 打开商城首页，登录个人账号，购买指定商品
        self.assertTrue(self.login_page.open_browser(config.OSMS_MALL_URL),u"打开商城首页失败~")

        r = self.mall_page.login(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.mall_page.search(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.place_order_page.buy_it_now_normal(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.place_order_page.order_settlement(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)
        order_number = r.ordernumber

        # 打开登录首页，登录联盟店用户， 发货，确认收款
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_shop)
        self.assertTrue(r.result, r.msg)

        r = self.order_settlement_page.delivery(order_number)
        self.assertTrue(r.result, r.msg)

        r = self.order_settlement_page.confirm_receipt(order_number)
        self.assertTrue(r.result, r.msg)

        #打开登录首页，登录个人用户，退货
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.goods_bought.returns(order_number)
        self.assertTrue(r.result, r.msg)

        # 打开登录首页，登录联盟店用户， 审批退货申请
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_shop)
        self.assertTrue(r.result, r.msg)

        r = self.approval_return_page.approval(order_number)
        self.assertTrue(r.result, r.msg)

    def test_returns_case2(self):
        u'''测试退货流程, 联盟店驳回'''

        # 打开商城首页，登录个人账号，购买指定商品
        self.assertTrue(self.login_page.open_browser(config.OSMS_MALL_URL),u"打开商城首页失败~")

        r = self.mall_page.login(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.mall_page.search(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.place_order_page.buy_it_now_normal(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.place_order_page.order_settlement(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)
        order_number = r.ordernumber

        # 打开登录首页，登录联盟店用户， 发货，确认收款
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_shop)
        self.assertTrue(r.result, r.msg)

        r = self.order_settlement_page.delivery(order_number)
        self.assertTrue(r.result, r.msg)

        r = self.order_settlement_page.confirm_receipt(order_number)
        self.assertTrue(r.result, r.msg)

        #打开登录首页，登录个人用户，退货
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.goods_bought.returns(order_number)
        self.assertTrue(r.result, r.msg)

        # 打开登录首页，登录联盟店用户， 审批退货申请
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败~")

        r = self.login_page.login(**test_returns_case1_shop)
        self.assertTrue(r.result, r.msg)

        r = self.approval_return_page.approval(order_number, approval_option=u'驳回')
        self.assertTrue(r.result, r.msg)