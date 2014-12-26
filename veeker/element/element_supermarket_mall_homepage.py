#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementMallHomepage(object):

    #今日订单
    today_order = (By.CSS_SELECTOR,u"div.huiyuan_left span a")

    #月订单
    month_order = (By.CSS_SELECTOR,u"div.huiyuan_right span a")

