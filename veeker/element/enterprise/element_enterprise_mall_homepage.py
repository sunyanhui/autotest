#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#今日订单
today_order = (By.CSS_SELECTOR, "div.service_right p b")

#月订单
month_order = (By.CSS_SELECTOR, "div.huiyuan_right span a")

#切换城市
change_city = (By.ID, 'changeArea')

#选择地区
area = (By.CLASS_NAME, 'weather-city')

#更换按钮
change_button = (By.CLASS_NAME, 'gh_btn')