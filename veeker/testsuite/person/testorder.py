#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 

import sys
import os
import unittest
import time

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from script import slogin, sbrowser
from script.person import splaceorder
from testdata.dorder import *


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.drive = sbrowser.Browser().openbrowser

    def tearDown(self):
        time.sleep(1)
        self.drive.quit()

    def test_order_case1(self):
        driver = self.drive

        loginresult = slogin.Login(driver).login(**test_order_case1)
        self.assertEqual(True, loginresult['result'], loginresult['msg'])

        findgoodsresult = splaceorder.PlaceOrder(driver).find_goods(**test_order_case1)
        self.assertEqual(True, findgoodsresult['result'], findgoodsresult['msg']+'\n'+findgoodsresult['img'])

        opengoodsdetailresult = splaceorder.PlaceOrder(driver).open_goodsdetail(**test_order_case1)
        self.assertEqual(True, opengoodsdetailresult['result'], opengoodsdetailresult['msg']+'\n'+opengoodsdetailresult['img'])

        buyitnowdetailresult = splaceorder.PlaceOrder(driver).buy_it_now(**test_order_case1)
        self.assertEqual(True, buyitnowdetailresult['result'], buyitnowdetailresult['msg']+'\n'+buyitnowdetailresult['img'])

        settlementresult = splaceorder.PlaceOrder(driver).order_settlement(**test_order_case1)
        self.assertEqual(True, settlementresult['result'], settlementresult['msg']+'\n'+settlementresult['img'])
        #print settlementresult['ordernumber']



