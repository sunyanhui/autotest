#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.olsm.data_enterprise_modify_vip_grade import *
from action.action_login import Login
from action.enterprise.action_enterprise_modify_vip_grade import EnterpriseModifyVipGrade
from common import config
import unittest
import logging
import time

class TestEnterpriseModifyVipGrade(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login = Login()
        self.enterprise_modify_vip_grade = EnterpriseModifyVipGrade()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_modifypass_case1(self):
        u'''测试正常情况下，企业修改会员等级'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modify_vip_grade_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.enterprise_modify_vip_grade.modify_vip_grade(**test_modify_vip_grade_case1)
        self.assertTrue(r['result'], r['msg'])


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestEnterpriseModifyVipGrade))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()