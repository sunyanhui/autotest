#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
import time
from common import config
from testdata.olsm.data_person_order import *
from action.action_login import Login
from action.person.action_person_find_goods import FindGoods
from action.person.action_person_place_order import PlaceOrder
from action.person.action_person_order_query import OrderQuery
from action.enterprise.action_enterprise_customer_order_settlement import EnterpriseCustomerOrderSettlement
from action.enterprise.action_enterprise_customer_order_query import EnterpriseCustomerOrderQuery
from action.enterprise.action_enterprise_mall_homepage import MallHomePage
from action.agency.action_agency_customer_order_settlement import AgencyCustomerOrderSettlement

class TestOrder(unittest.TestCase):
    u'''
    测试下订单
    '''
    def setUp(self):
        self.loginPage = Login()
        self.findGoodsPage = FindGoods()
        self.placeOrderPage = PlaceOrder()
        self.orderQueryPage = OrderQuery()
        self.enterpriseCustomerOrderSettlementPage = EnterpriseCustomerOrderSettlement()
        self.enterpriseCustomerOrderQueryPage = EnterpriseCustomerOrderQuery()
        self.agencyCustomerOrderSettlementPage = AgencyCustomerOrderSettlement()
        self.mallHomePage = MallHomePage()

    # def tearDown(self):
    #     time.sleep(1)
    #     self.loginPage.quit()

    def test_order_case1(self):
        u'''验证下订单流程(企业商城正常商品、无联盟店)'''

        self.assertTrue(self.loginPage.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.loginPage.login(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_normal(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**test_order_case1_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), test_order_case1_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case1_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**test_order_case1_enterprise)
        self.assertTrue(r.result, r.msg)

        r = self.enterpriseCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

    def test_order_case2(self):
        u'''验证下订单流程(企业商城团购商品、无联盟店)'''

        self.assertTrue(self.loginPage.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.loginPage.login(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_group(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**test_order_case2_person)
        self.assertTrue(r.result, r.msg)

        self.assertEqual(float(r.totalPrice), test_order_case2_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case2_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**test_order_case2_enterprise)
        self.assertTrue(r.result, r.msg)

        r = self.enterpriseCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

    def test_order_case3(self):
        u'''验证下订单流程(企业商城打折商品、无联盟店)'''

        self.assertTrue(self.loginPage.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.loginPage.login(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_normal(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**test_order_case3_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), test_order_case3_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), test_order_case3_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**test_order_case3_enterprise)
        self.assertTrue(r.result, r.msg)

        r = self.enterpriseCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)


    def test_order_case4(self):
        u'''验证企业商场首页今日订单和月订单功能'''

        r = self.mallHomePage.order_number(config.OLSM_MALL_URL)
        self.assertTrue(r.result, r.msg)
        before = int(r.today_order)

        self.assertTrue(self.loginPage.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.loginPage.login(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_normal(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**test_order_case4)
        self.assertTrue(r.result, r.msg)

        r = self.mallHomePage.order_number(config.OLSM_MALL_URL)
        self.assertTrue(r.result, r.msg)
        after = int(r.today_order)

        self.assertEqual(after - before, 1, u"今日订单数量验证失败")

    def test_order_case5(self):
        u'''验证下订单流程(企业商城正常商品、无分销商)，企业发货、个人确认收货后，企业确认收款'''
        data_person = test_order_case1_person
        data_supermarket = test_order_case1_enterprise

        #打开首页
        self.assertTrue(self.loginPage.open_browser(config.OLMS_URL),u"打开首页失败")

        #登录个人账号
        r = self.loginPage.login(**data_person)
        self.assertTrue(r.result, r.msg)

        #找到要下订单的商品，并打开
        r = self.findGoodsPage.find_goods(**data_person)
        self.assertTrue(r.result, r.msg)

        #打开下订单页面
        r = self.placeOrderPage.buy_it_now_normal(**data_person)
        self.assertTrue(r.result, r.msg)

        #下订单
        r = self.placeOrderPage.order_settlement(**data_person)
        self.assertTrue(r.result, r.msg)

        #检查订单总额与总价
        self.assertEqual(float(r.totalPrice), data_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), data_person.goodsprice, u'应付总额与商品定价不符')

        #获取订单号
        ordernumber = r.ordernumber

        #登出
        self.loginPage.logout()

        #登录超市
        r = self.loginPage.login(**data_supermarket)
        self.assertTrue(r.result, r.msg)

        #超市发货
        r = self.enterpriseCustomerOrderSettlementPage.send_out_goods(ordernumber)
        self.assertTrue(r.result, r.msg)

        #登出
        self.loginPage.logout()

        #登录个人
        r = self.loginPage.login(**data_person)
        self.assertTrue(r.result, r.msg)

        #确认收货
        r = self.orderQueryPage.confirm_receipt(ordernumber)
        self.assertTrue(r.result, r.msg)

        #登出
        r = self.loginPage.logout()
        self.assertTrue(r.result, r.msg)

        #登录超市
        r = self.loginPage.login(**data_supermarket)
        self.assertTrue(r.result, r.msg)

        #超市发货
        r = self.enterpriseCustomerOrderSettlementPage.confirm_receipt(ordernumber)
        self.assertTrue(r.result, r.msg)

        #超市查询该订单
        r = self.enterpriseCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

    def test_order_case6(self):
        u'''验证下订单流程(企业商城打折商品、有县级分销商)'''

        data_person = test_order_case6_person
        data_agency = test_order_case6_agency

        self.assertTrue(self.loginPage.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.loginPage.login(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_normal(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**data_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), data_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), data_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**data_agency)
        self.assertTrue(r.result, r.msg)

        r = self.agencyCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

    def test_order_case7(self):
        u'''验证下订单流程(企业商城团购商品、有市级分销商)'''

        data_person = test_order_case7_person
        data_agency = test_order_case7_agency

        self.assertTrue(self.loginPage.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.loginPage.login(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_group(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**data_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), data_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), data_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**data_agency)
        self.assertTrue(r.result, r.msg)

        r = self.agencyCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

    def test_order_case8(self):
        u'''验证下订单流程(企业商城正常商品、有省级分销商)'''

        data_person = test_order_case8_person
        data_agency = test_order_case8_agency

        self.assertTrue(self.loginPage.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.loginPage.login(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.findGoodsPage.find_goods(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.buy_it_now_normal(**data_person)
        self.assertTrue(r.result, r.msg)

        r = self.placeOrderPage.order_settlement(**data_person)
        self.assertTrue(r.result, r.msg)
        self.assertEqual(float(r.totalPrice), data_person.goodsprice, u'总价与商品定价不符')
        self.assertEqual(float(r.shouldPayPrice), data_person.goodsprice, u'应付总额与商品定价不符')
        ordernumber = r.ordernumber

        r = self.orderQueryPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

        self.loginPage.logout()
        r = self.loginPage.login(**data_agency)
        self.assertTrue(r.result, r.msg)

        r = self.agencyCustomerOrderSettlementPage.if_order_exist(ordernumber)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    from common import HTMLTestRunner
    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestOrder))
    runner = HTMLTestRunner.HTMLTestRunner(stream=open('test.html','wb'), title=u'测试报告', description=u'测试报告')
    runner.run(a)