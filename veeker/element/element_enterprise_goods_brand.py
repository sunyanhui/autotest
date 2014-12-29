#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementGoodsBrand(object):

    #商品品牌链接
    goods_brand_link = (By.LINK_TEXT,u"企业品牌管理")

    #保存按钮
    save_button = (By.CLASS_NAME,u"btn_tjmm")

    #添加按钮
    add_button = (By.CLASS_NAME,u"csbtn_tj")

    #删除链接
    del_link = (By.XPATH,u"//input[@value='%s']/../a")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #品牌名称输入框
    brand_name = (By.NAME,u"brandName")

