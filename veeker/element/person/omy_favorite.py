#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#***********************我的收藏***********************#
#我的收藏链接
myFavorites = (By.LINK_TEXT, u'我的收藏')

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#商品收藏
goodscollect = (By.LINK_TEXT, u'商品收藏')

#商家收藏
shopscollect = (By.LINK_TEXT, u'商家收藏')

#下一页
nextpage = (By.LINK_TEXT, u'下一页')

#OK按钮
okButton = (By.ID, 'popup_ok')