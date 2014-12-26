#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementCustomerOrderQuery(object):

    #客户订单结算查询
    customerOrderSettlement = (By.LINK_TEXT,u"客户订单结算")

    #客户订单查询
    customerOrderQuery = (By.LINK_TEXT,u"客户订单查询")

    #订单编号
    order_number = (By.ID,u"orderNo")

    #搜索按钮
    search = (By.CLASS_NAME,u"cgdd_btn_cx")

    #发货链接
    sendOutGoods = (By.LINK_TEXT,u"发货")

    #确认收款链接
    confirmReceipt = (By.LINK_TEXT,u"确认收款")

    #确定按钮
    confirm = (By.ID,u"pop_confirm")

