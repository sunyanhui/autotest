#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.data_order import *
from action.slogin import Login
from action.person.sfind_goods import FindGoods
from action.person.splace_order import PlaceOrder
from action.person.sorder_query import OrderQuery
from action.supermarket.customer_order_settlement import CustomerOrderSettlement
from common import config
import unittest
import logging
import time

class TestOrder(unittest.TestCase):
    u'''
    测试注册
    '''
    def setUp(self):
        self.login = Login()
        self.findGoods = FindGoods()
        self.placeOrder = PlaceOrder()
        self.orderQuery = OrderQuery()
        self.customerOrderSettlement = CustomerOrderSettlement()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()

    def test_order(self):

        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        r1 = self.login.login(**test_order_case1_person)
        self.assertTrue(r1['result'], r1['msg'])

        r2 = self.findGoods.find_goods(**test_order_case1_person)
        self.assertTrue(r2['result'], r2['msg'])

        r3 = self.placeOrder.buy_it_now(**test_order_case1_person)
        self.assertTrue(r3['result'], r3['msg'])

        r4 = self.placeOrder.order_settlement(**test_order_case1_person)
        self.assertTrue(r4['result'], r4['msg'])
        self.assertEqual(float(r4['totalPrice']), test_order_case1_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r4['shouldPayPrice']), test_order_case1_person['goodsprice'], u'应付总额与商品定价不符')

        r5 = self.orderQuery.if_order_exist(r4['ordernumber'])
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**test_order_case1_supermarket)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.customerOrderSettlement.if_order_exist(r4['ordernumber'])
        self.assertTrue(r7['result'], r7['msg'])



if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    from common import HTMLTestRunner
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOrder))
    runner = HTMLTestRunner.HTMLTestRunner(stream=open('test.html','wb'), title=u'测试报告', description=u'测试报告')
    runner.run(a)