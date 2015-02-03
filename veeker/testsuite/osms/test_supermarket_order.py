#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
import time
from common import config
from testdata.osms.data_person_order import *
from action.action_login import Login
from action.person.action_person_find_goods import FindGoods
from action.person.action_person_place_order import PlaceOrder
from action.person.action_person_order_query import OrderQuery
from action.supermarket.action_supermarket_customer_order_settlement import SupermarketCustomerOrderSettlement
from action.supermarket.action_supermarket_customer_order_query import SupermarketCustomerOrderQuery
from action.shop.action_shop_customer_order_settlement import ShopCustomerOrderSettlement
from action.supermarket.action_supermarket_mall_homepage import MallHomePage



class TestOrder(unittest.TestCase):
    u'''
    测试下订单
    '''
    def setUp(self):
        self.login = Login()
        self.findGoods = FindGoods()
        self.placeOrder = PlaceOrder()
        self.orderQuery = OrderQuery()
        self.supermarketCustomerOrderSettlement = SupermarketCustomerOrderSettlement()
        self.supermarketCustomerOrderQuery = SupermarketCustomerOrderQuery()
        self.shopCustomerOrderSettlement = ShopCustomerOrderSettlement()
        self.mallHomePage = MallHomePage()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_order_case1(self):
        u'''验证下订单流程(超市商城正常商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoods.find_goods(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.buy_it_now_normal(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.order_settlement(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), test_order_case1_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case1_person.goodsprice, u'应付总额与商品定价不符')

        order_number = r.ordernumber
        r = self.orderQuery.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

        self.login.logout()
        r = self.login.login(**test_order_case1_supermarket)
        self.assertTrue(r.result, r.msg)

        r = self.supermarketCustomerOrderSettlement.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

    def test_order_case2(self):
        u'''验证下订单流程(超市商城团购商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoods.find_goods(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.buy_it_now_group(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.order_settlement(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        self.assertEqual(float(r.totalPrice), test_order_case2_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case2_person.goodsprice, u'应付总额与商品定价不符')

        order_number = r.ordernumber
        r = self.orderQuery.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

        self.login.logout()
        r = self.login.login(**test_order_case2_supermarket)
        self.assertTrue(r.result, r.msg)

        r = self.supermarketCustomerOrderSettlement.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

    def test_order_case3(self):
        u'''验证下订单流程(超市商城打折商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoods.find_goods(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.buy_it_now_normal(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.order_settlement(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), test_order_case3_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case3_person.goodsprice, u'应付总额与商品定价不符')

        order_number = r.ordernumber
        r = self.orderQuery.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

        self.login.logout()
        r = self.login.login(**test_order_case3_supermarket)
        self.assertTrue(r.result, r.msg)

        r = self.supermarketCustomerOrderSettlement.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)


    def test_order_case4(self):
        u'''验证超市商场首页今日订单和月订单功能'''

        r = self.mallHomePage.order_number(config.OSMS_MALL_URL)
        self.assertTrue(r.result, r.msg)
        before_today = int(r.today_order)
        before_month = int(r.month_order)

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.findGoods.find_goods(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.buy_it_now_normal(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.order_settlement(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.mallHomePage.order_number(config.OSMS_MALL_URL)
        self.assertTrue(r.result, r.msg)

        after_today = int(r.today_order)
        after_month = int(r.month_order)

        self.assertEqual(after_today - before_today, 1, u"日订单数量验证失败")
        self.assertEqual(after_month - before_month, 1, u"月订单数量验证失败")


    def test_order_case5(self):
        u'''验证下订单流程(超市商城打折商品、有联盟店)'''

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**test_order_case5_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoods.find_goods(**test_order_case5_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.buy_it_now_normal(**test_order_case5_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrder.order_settlement(**test_order_case5_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), test_order_case5_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case5_person.goodsprice, u'应付总额与商品定价不符')
        order_number = r.ordernumber

        r = self.orderQuery.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)

        self.login.logout()
        r = self.login.login(**test_order_case5_shop)
        self.assertTrue(r.result, r.msg)

        r = self.shopCustomerOrderSettlement.if_order_exist(order_number)
        self.assertTrue(r.result, r.msg)


    def test_order_case6(self):
        u'''验证下订单流程(超市商城正常商品、无联盟店)，超市发货、个人确认收货后，超市确认收款'''
        data_person = test_order_case1_person
        data_supermarket = test_order_case1_supermarket

        #打开首页
        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        #登录个人账号
        r = self.login.login(**data_person)
        self.assertTrue(r.result, r.msg)

        #找到要下订单的商品，并打开
        r = self.findGoods.find_goods(**data_person)
        self.assertTrue(r.result, r.msg)

        #打开下订单页面
        r = self.placeOrder.buy_it_now_normal(**data_person)
        self.assertTrue(r.result, r.msg)

        #下订单
        r = self.placeOrder.order_settlement(**data_person)
        self.assertTrue(r.result, r.msg)

        #检查订单总额与总价
        self.assertEqual(float(r.totalPrice), data_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), data_person.goodsprice, u'应付总额与商品定价不符')

        #获取订单号
        ordernumber = r.ordernumber

        #登出
        self.login.logout()

        #登录超市
        r = self.login.login(**data_supermarket)
        self.assertTrue(r.result, r.msg)

        #超市发货
        r = self.supermarketCustomerOrderSettlement.send_out_goods(ordernumber)
        self.assertTrue(r.result, r.msg)

        #登出
        self.login.logout()

        #登录个人
        r = self.login.login(**data_person)
        self.assertTrue(r.result, r.msg)

        #确认收货
        r = self.orderQuery.confirm_receipt(ordernumber)
        self.assertTrue(r.result, r.msg)

        #登出
        r = self.login.logout()
        self.assertTrue(r.result, r.msg)

        #登录超市
        r = self.login.login(**data_supermarket)
        self.assertTrue(r.result, r.msg)

        #超市发货
        r = self.supermarketCustomerOrderSettlement.confirm_receipt(ordernumber)
        self.assertTrue(r.result, r.msg)

        #超市查询该订单
        r = self.supermarketCustomerOrderQuery.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    from common import HTMLTestRunner
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOrder))
    runner = HTMLTestRunner.HTMLTestRunner(stream=open('test.html','wb'), title=u'测试报告', description=u'测试报告')
    runner.run(a)