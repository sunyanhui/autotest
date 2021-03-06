#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementCustomerOrderSettlement(object):

    #客户订单结算查询
    customerOrderSettlement = (By.LINK_TEXT,u"客户订单结算")

    #订单编号
    order_number = (By.ID,u"orderNo")

    #搜索按钮
    search = (By.CLASS_NAME,u"searchbtn")

    #物流名称
    logistics_name = (By.ID,u"pop_shipName")

    #物流编号
    logistics_number = (By.ID,u"pop_shipCode")

    #确认
    confirm = (By.ID,u"pop_confirm")

