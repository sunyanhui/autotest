#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#购物车左栏链接
goodscart = (By.LINK_TEXT, u'购物车')

#我的购物车链接
mygoodscart = (By.LINK_TEXT, u'我的购物车')

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u"下一页")

#温馨提示
prompt = (By.ID, 'popup_message')

#确定键
okButton = (By.ID, 'popup_ok')