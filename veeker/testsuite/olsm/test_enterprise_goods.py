#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_goods import *
from action.action_login import Login
from action.enterprise.action_enterprise_release_goods import EnterpriseReleaseGoods
from action.enterprise.action_enterprise_release_group import EnterpriseReleaseGroup
from action.enterprise.action_enterprise_goods_in_storage import EnterpriseGoodsInStorage
from action.enterprise.action_enterprise_goods_on_sale import EnterpriseGoodsOnsale
import unittest
import time

class TestEnterpriseGoods(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.release_goods_page = EnterpriseReleaseGoods()
        self.release_group_page = EnterpriseReleaseGroup()
        self.enterprise_goods_in_storage = EnterpriseGoodsInStorage()
        self.enterprise_goods_on_sale = EnterpriseGoodsOnsale()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_goods_case1(self):

        u'''企业发布普通商品；
        点击“在售商品”链接，进入后找到该商品，然后下架
        点击“仓库中的商品”链接，进入后找到该商品，上架，下架，然后删除'''
        self.assertTrue(self.login_page.open_browser(config.OLMS_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**test_goods_case1)
        self.assertTrue(r.result, r.msg)

        #发布商品
        r = self.release_goods_page.release_goods()
        self.assertTrue(r.result, r.msg)
        goods_name = r.goods_name

        #在在售商品页面 下架 商品
        r = self.enterprise_goods_on_sale.xiajia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面上架商品
        r = self.enterprise_goods_in_storage.shangjia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面下架商品
        r = self.enterprise_goods_in_storage.xiajia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面删除商品
        r = self.enterprise_goods_in_storage.delete(goods_name)
        self.assertTrue(r.result, r.msg)

    def test_goods_case2(self):

        u'''企业发布团购商品；
        点击“在售商品”链接，进入后找到该商品，然后下架
        点击“仓库中的商品”链接，进入后找到该商品，上架，下架，然后删除'''
        self.assertTrue(self.login_page.open_browser(config.OLMS_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**test_goods_case1)
        self.assertTrue(r.result, r.msg)

        #发布团购商品
        r = self.release_group_page.release_group()
        self.assertTrue(r.result, r.msg)
        goods_name = r.goods_name

        #在在售商品页面 下架 商品
        r = self.enterprise_goods_on_sale.xiajia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面上架商品
        r = self.enterprise_goods_in_storage.shangjia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面下架商品
        r = self.enterprise_goods_in_storage.xiajia(goods_name)
        self.assertTrue(r.result, r.msg)

        #在仓库中的商品页面删除商品
        r = self.enterprise_goods_in_storage.delete(goods_name)
        self.assertTrue(r.result, r.msg)