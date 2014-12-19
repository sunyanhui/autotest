#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementBrandManage(object):

    #品牌管理链接
    brand_manage_link = (By.LINK_TEXT,u"企业品牌管理")

    #品牌名称
    brand_name = (By.NAME,u"brandName")

    #保存按钮
    save_button = (By.CLASS_NAME,u"btn_tjmm")

    #删除链接
    del_link = (By.LINK_TEXT,u"删除")

    #添加按钮
    add_button = (By.CLASS_NAME,u"csbtn_tj")

