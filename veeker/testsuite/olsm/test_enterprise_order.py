#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
import time

from testdata.olsm.data_person_order import *
from action.action_login import Login
from action.person.sfind_goods import FindGoods
from action.person.action_person_place_order import PlaceOrder
from action.person.action_person_order_query import OrderQuery
from action.enterprise.action_enterprise_customer_order_settlement import EnterpriseCustomerOrderSettlement
from action.enterprise.action_enterprise_customer_order_query import EnterpriseCustomerOrderQuery
from action.enterprise.action_enterprise_mall_homepage import MallHomePage
from action.agency.action_agency_customer_order_settlement import AgencyCustomerOrderSettlement
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
        self.enterpriseCustomerOrderSettlement = EnterpriseCustomerOrderSettlement()
        self.enterpriseCustomerOrderQuery = EnterpriseCustomerOrderQuery()
        self.agencyCustomerOrderSettlement = AgencyCustomerOrderSettlement()
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

        r7 = self.enterpriseCustomerOrderSettlement.if_order_exist(r4['ordernumber'])
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

        r7 = self.enterpriseCustomerOrderSettlement.if_order_exist(r4['ordernumber'])
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

        r7 = self.enterpriseCustomerOrderSettlement.if_order_exist(r4['ordernumber'])
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

    def test_order_case5(self):
        u'''验证下订单流程(企业商城正常商品、无分销商)，企业发货、个人确认收货后，企业确认收款'''
        data_person = test_order_case1_person
        data_supermarket = test_order_case1_enterprise

        #打开首页
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")

        #登录个人账号
        r = self.login.login(**data_person)
        self.assertTrue(r['result'], r['msg'])

        #找到要下订单的商品，并打开
        r = self.findGoods.find_goods(**data_person)
        self.assertTrue(r['result'], r['msg'])

        #打开下订单页面
        r = self.placeOrder.buy_it_now_normal(**data_person)
        self.assertTrue(r['result'], r['msg'])

        #下订单
        r = self.placeOrder.order_settlement(**data_person)
        self.assertTrue(r['result'], r['msg'])

        #检查订单总额与总价
        self.assertEqual(float(r['totalPrice']), data_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r['shouldPayPrice']), data_person['goodsprice'], u'应付总额与商品定价不符')

        #获取订单号
        ordernumber = r['ordernumber']

        #登出
        self.login.logout()

        #登录超市
        r = self.login.login(**data_supermarket)
        self.assertTrue(r['result'], r['msg'])

        #超市发货
        r = self.enterpriseCustomerOrderSettlement.send_out_goods(ordernumber)
        self.assertTrue(r['result'], r['msg'])

        #登出
        self.login.logout()

        #登录个人
        r = self.login.login(**data_person)
        self.assertTrue(r['result'], r['msg'])

        #确认收货
        r = self.orderQuery.confirm_receipt(ordernumber)
        self.assertTrue(r['result'], r['msg'])

        #登出
        r = self.login.logout()
        self.assertTrue(r['result'], r['msg'])

        #登录超市
        r = self.login.login(**data_supermarket)
        self.assertTrue(r['result'], r['msg'])

        #超市发货
        r = self.enterpriseCustomerOrderSettlement.confirm_receipt(ordernumber)
        self.assertTrue(r['result'], r['msg'])

        #超市查询该订单
        r = self.enterpriseCustomerOrderSettlement.if_order_exist(ordernumber)
        self.assertTrue(r['result'], r['msg'])

    def test_order_case6(self):
        u'''验证下订单流程(企业商城打折商品、有县级分销商)'''

        data_person = test_order_case6_person
        data_agency = test_order_case6_agency

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.findGoods.find_goods(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.buy_it_now_normal(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.order_settlement(**data_person)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(float(r['totalPrice']), data_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r['shouldPayPrice']), data_person['goodsprice'], u'应付总额与商品定价不符')
        ordernumber = r['ordernumber']

        r5 = self.orderQuery.if_order_exist(ordernumber)
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**data_agency)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.agencyCustomerOrderSettlement.if_order_exist(ordernumber)
        self.assertTrue(r7['result'], r7['msg'])

    def test_order_case7(self):
        u'''验证下订单流程(企业商城团购商品、有市级分销商)'''

        data_person = test_order_case7_person
        data_agency = test_order_case7_agency

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.findGoods.find_goods(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.buy_it_now_group(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.order_settlement(**data_person)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(float(r['totalPrice']), data_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r['shouldPayPrice']), data_person['goodsprice'], u'应付总额与商品定价不符')
        ordernumber = r['ordernumber']

        r5 = self.orderQuery.if_order_exist(ordernumber)
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**data_agency)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.agencyCustomerOrderSettlement.if_order_exist(ordernumber)
        self.assertTrue(r7['result'], r7['msg'])

    def test_order_case8(self):
        u'''验证下订单流程(企业商城正常商品、有省级分销商)'''

        data_person = test_order_case8_person
        data_agency = test_order_case8_agency

        self.assertTrue(self.login.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login.login(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.findGoods.find_goods(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.buy_it_now_normal(**data_person)
        self.assertTrue(r['result'], r['msg'])

        r = self.placeOrder.order_settlement(**data_person)
        self.assertTrue(r['result'], r['msg'])
        self.assertEqual(float(r['totalPrice']), data_person['goodsprice'], u'总价与商品定价不符')
        self.assertEqual(float(r['shouldPayPrice']), data_person['goodsprice'], u'应付总额与商品定价不符')
        ordernumber = r['ordernumber']

        r5 = self.orderQuery.if_order_exist(ordernumber)
        self.assertTrue(r5['result'], r5['msg'])

        self.login.logout()
        r6 = self.login.login(**data_agency)
        self.assertTrue(r6['result'], r6['msg'])

        r7 = self.agencyCustomerOrderSettlement.if_order_exist(ordernumber)
        self.assertTrue(r7['result'], r7['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    from common import HTMLTestRunner
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOrder))
    runner = HTMLTestRunner.HTMLTestRunner(stream=open('test.html','wb'), title=u'测试报告', description=u'测试报告')
    runner.run(a)