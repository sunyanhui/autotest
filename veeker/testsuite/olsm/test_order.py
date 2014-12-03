#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
import time

from testdata.olsm.data_order import *
from action.slogin import Login
from action.person.sfind_goods import FindGoods
from action.person.splace_order import PlaceOrder
from action.person.sorder_query import OrderQuery
from action.enterprise.customer_order_settlement import CustomerOrderSettlement
from action.enterprise.mall_homepage import MallHomePage
from common import config


class TestOrder(unittest.TestCase):
    u'''
    测试下订单
    '''
    def setUp(self):
        self.login = Login()
        self.findGoods = FindGoods()
        self.placeOrder = PlaceOrder()
        self.orderQuery = OrderQuery()
        self.customerOrderSettlement = CustomerOrderSettlement()
        self.mallHomePage = MallHomePage()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_order_case1(self):
        u'''验证下订单流程(企业商城正常商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        r1 = self.login.login(**test_order_case1_person)
        self.assertTrue(r1['result'], r1['msg'])

        r2 = self.findGoods.find_goods(**test_order_case1_person)
        self.assertTrue(r2['result'], r2['msg'])

        r3 = self.placeOrder.buy_it_now_normal(**test_order_case1_person)
        self.assertTrue(r3['result'], r3['msg'])

        r4 = self.placeOrder.order_settlement(**test_order_case1_person)
        self.assertTrue(r4['result'], r4['msg'])
        self.assertEqual(float(r4['totalPrice']), test_order_case1_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r4['shouldPayPrice']), test_order_case1_person['goodsprice'], u'应付总额与商品定价不符')

        r5 = self.orderQuery.if_order_exist(r4['ordernumber'])
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**test_order_case1_enterprise)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.customerOrderSettlement.if_order_exist(r4['ordernumber'])
        self.assertTrue(r7['result'], r7['msg'])

    def test_order_case2(self):
        u'''验证下订单流程(企业商城团购商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        r1 = self.login.login(**test_order_case2_person)
        self.assertTrue(r1['result'], r1['msg'])

        r2 = self.findGoods.find_goods(**test_order_case2_person)
        self.assertTrue(r2['result'], r2['msg'])

        r3 = self.placeOrder.buy_it_now_group(**test_order_case2_person)
        self.assertTrue(r3['result'], r3['msg'])

        r4 = self.placeOrder.order_settlement(**test_order_case2_person)
        self.assertTrue(r4['result'], r4['msg'])

        self.assertEqual(float(r4['totalPrice']), test_order_case2_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r4['shouldPayPrice']), test_order_case2_person['goodsprice'], u'应付总额与商品定价不符')

        r5 = self.orderQuery.if_order_exist(r4['ordernumber'])
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**test_order_case2_enterprise)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.customerOrderSettlement.if_order_exist(r4['ordernumber'])
        self.assertTrue(r7['result'], r7['msg'])

    def test_order_case3(self):
        u'''验证下订单流程(企业商城打折商品、无联盟店)'''

        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        r1 = self.login.login(**test_order_case3_person)
        self.assertTrue(r1['result'], r1['msg'])

        r2 = self.findGoods.find_goods(**test_order_case3_person)
        self.assertTrue(r2['result'], r2['msg'])

        r3 = self.placeOrder.buy_it_now_normal(**test_order_case3_person)
        self.assertTrue(r3['result'], r3['msg'])

        r4 = self.placeOrder.order_settlement(**test_order_case3_person)
        self.assertTrue(r4['result'], r4['msg'])
        self.assertEqual(float(r4['totalPrice']), test_order_case3_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r4['shouldPayPrice']), test_order_case3_person['goodsprice'], u'应付总额与商品定价不符')

        r5 = self.orderQuery.if_order_exist(r4['ordernumber'])
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**test_order_case3_enterprise)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.customerOrderSettlement.if_order_exist(r4['ordernumber'])
        self.assertTrue(r7['result'], r7['msg'])


    def test_order_case4(self):
        u'''验证企业商场首页今日订单和月订单功能'''

        r0 = self.mallHomePage.order_number(config.OLSM_MALL_URL)
        self.assertTrue(r0['result'], r0['msg'])

        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        r1 = self.login.login(**test_order_case4)
        self.assertTrue(r1['result'], r1['msg'])

        r2 = self.findGoods.find_goods(**test_order_case4)
        self.assertTrue(r2['result'], r2['msg'])

        r3 = self.placeOrder.buy_it_now_normal(**test_order_case4)
        self.assertTrue(r3['result'], r3['msg'])

        r4 = self.placeOrder.order_settlement(**test_order_case4)
        self.assertTrue(r4['result'], r4['msg'])

        r5 = self.mallHomePage.order_number(config.OLSM_MALL_URL)
        self.assertTrue(r5['result'], r5['msg'])

        self.assertEqual(int(r5['today_order']) - int(r0['today_order']), 1, u"今日订单数量验证失败")

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    from common import HTMLTestRunner
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOrder))
    runner = HTMLTestRunner.HTMLTestRunner(stream=open('test.html','wb'), title=u'测试报告', description=u'测试报告')
    runner.run(a)