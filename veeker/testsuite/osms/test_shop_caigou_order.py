#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_shop_caigou_order import *
from action.action_login import Login
from action.shop.action_shop_add_order import ShopAddOrder
from action.shop.action_shop_supply_order import ShopSupplyOrder
import unittest
import time


class TestShopCaigouOrder(unittest.TestCase):
    """测试联盟店添加采购单"""


    def setUp(self):
        self.login_page = Login()
        self.add_order_page = ShopAddOrder()
        self.supply_order_page = ShopSupplyOrder()

    # def tearDown(self):
    #     self.login_page.quit()

    def test_business_cooperation_case1(self):
        u"""测试联盟店正常添加采购单"""

        case = test_shop_caigou_order_case1
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #获取采购订单数量
        r = self.supply_order_page.get_num()
        self.assertTrue(r.result, r.msg)
        num1 = int(r.num)

        # 提交采购单
        r = self.add_order_page.add()
        self.assertTrue(r.result, r.msg)

        #获取采购订单数量
        r = self.supply_order_page.get_num()
        self.assertTrue(r.result, r.msg)
        num2 = int(r.num)

        self.assertEqual(1,num2-num1,u"下单成功，订单数据没有增加")

    def test_business_cooperation_case2(self):
        u"""测试发布采购单"""

        case = test_shop_caigou_order_case2
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        # 撤销采购单
        r = self.supply_order_page.publish()
        self.assertTrue(r.result, r.msg)

    def test_business_cooperation_case3(self):
        u"""测试删除采购单"""

        case = test_shop_caigou_order_case3
        self.assertTrue(self.login_page.open_browser(config.BASE_URL), u"打开首页失败")

        # 登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        # 提交采购单
        r = self.add_order_page.add()
        self.assertTrue(r.result, r.msg)

        # 删除采购单
        r = self.supply_order_page.del_order()
        self.assertTrue(r.result, r.msg)