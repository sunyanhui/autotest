#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_picture_space import *
from action.action_login import Login
from action.supermarket.action_supermarket_picture_space import SupermarketPictureSpace
import unittest
import time

class TestSupermarketPictureSpace(unittest.TestCase):
    u'''
    测试超市图片空间
    '''
    def setUp(self):
        self.login_page = Login()
        self.picture_space_page = SupermarketPictureSpace()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_picture_space_case1(self):
        u'''测试超市图片空间上传图片'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_picture_space_case1)
        self.assertTrue(r.result, r.msg)

        r = self.picture_space_page.add_picture()
        self.assertTrue(r.result, r.msg)

    def test_picture_space_case2(self):
        u'''测试超市图片空间删除图片'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_picture_space_case1)
        self.assertTrue(r.result, r.msg)

        r = self.picture_space_page.del_picture()
        self.assertTrue(r.result, r.msg)

    def test_picture_space_case3(self):
        u'''测试超市图片空间清空回收站'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_picture_space_case1)
        self.assertTrue(r.result, r.msg)

        r = self.picture_space_page.empty()
        self.assertTrue(r.result, r.msg)