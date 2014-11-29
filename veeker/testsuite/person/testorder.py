#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 

import sys
import os
import unittest
import time

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from action import slogin, sbrowser
from action.person import splace_order
from testdata.dorder import *


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.login = slogin.Login()
        self.place_order =splace_order.PlaceOrder()
        self.login.open_browser("http://www.wiki100.cn")

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_order_case1(self):

        loginresult = self.login.login(**test_order_case1)
        self.assertEqual(True, loginresult['result'], loginresult['msg'])

        findgoodsresult = self.place_order.find_goods(**test_order_case1)
        self.assertEqual(True, findgoodsresult['result'], findgoodsresult['msg']+'\n'+findgoodsresult['img'])

        opengoodsdetailresult = self.place_order.open_goodsdetail(**test_order_case1)
        self.assertEqual(True, opengoodsdetailresult['result'], opengoodsdetailresult['msg']+'\n'+opengoodsdetailresult['img'])

        buyitnowdetailresult = self.place_order.buy_it_now(**test_order_case1)
        self.assertEqual(True, buyitnowdetailresult['result'], buyitnowdetailresult['msg']+'\n'+buyitnowdetailresult['img'])

        settlementresult = self.place_order.order_settlement(**test_order_case1)
        self.assertEqual(True, settlementresult['result'], settlementresult['msg']+'\n'+settlementresult['img'])
        #print settlementresult['ordernumber']



