#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementGoodsInStorage(object):

    #上架
    shangjia_button = (By.CSS_SELECTOR,u"input[value='上架'][class='sj_bgcolor']")

    #删除商品
    delete_link = (By.LINK_TEXT,u"删除商品")

    #仓库中的商品链接
    goods_in_storage = (By.LINK_TEXT,u"仓库中的商品")

    #商品名称
    goods_name = (By.ID,u"goodsname")

    #搜索按钮
    search = (By.ID,u"tijiao")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #下架
    xiajia_button = (By.CSS_SELECTOR,u"input[value='下架'][class='sj_bgcolor']")

