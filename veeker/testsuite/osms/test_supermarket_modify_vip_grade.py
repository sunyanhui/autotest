#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_modify_vip_grade import *
from action.action_login import Login
from action.supermarket.action_supermarket_modify_vip_grade import SupermarketModifyVipGrade
import unittest
import logging
import time

class TestSupermarketModifyVipGrade(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login_page = Login()
        self.modify_vip_grade_page = SupermarketModifyVipGrade()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()


    def test_modify_vip_grade_case1(self):
        u'''测试正常情况下，超市修改会员等级'''
        self.assertTrue(self.login_page.open_browser(config.OLMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_modify_vip_grade_case1)
        self.assertTrue(r.result, r.msg)
        
        r = self.modify_vip_grade_page.modify_vip_grade(**test_modify_vip_grade_case1)
        self.assertTrue(r.result, r.msg)


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketModifyVipGrade))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()