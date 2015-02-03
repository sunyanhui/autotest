#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.olsm.data_enterprise_notice import *
from action.action_login import Login
from action.enterprise.action_enterprise_notice import EnterpriseNotice
import unittest
import time

class TestEnterpriseNotice(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.notice_page = EnterpriseNotice()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_notice_case1(self):
        u'''测试企业添加通知公告并删除'''
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        r = self.login_page.login(**test_notice_case1)
        self.assertTrue(r.result, r.msg)

        r = self.notice_page.add_notice()
        self.assertTrue(r.result, r.msg)
        title = r.title

        r = self.notice_page.del_notice(title)
        self.assertTrue(r.result, r.msg)