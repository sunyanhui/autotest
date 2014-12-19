#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementGoodsOnsale(object):

    #下架
    xiajia_link = (By.LINK_TEXT,u"下架")

    #出售中的商品链接
    goods_onsale = (By.LINK_TEXT,u"出售中的商品")

