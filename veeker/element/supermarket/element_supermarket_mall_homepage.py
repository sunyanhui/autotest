#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#今日订单
today_order = (By.CSS_SELECTOR, "div.huiyuan_left span a")

#月订单
month_order = (By.CSS_SELECTOR, "div.huiyuan_right span a")

