#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#客户订单结算查询
customerOrderSettlement = (By.LINK_TEXT, u'客户订单结算')

#订单编号
order_number = (By.ID, 'orderNo')

#搜索按钮
search = (By.CLASS_NAME, 'search_btn')