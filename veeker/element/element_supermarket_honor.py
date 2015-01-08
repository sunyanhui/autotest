#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementHonor(object):

    #增加资质
    add_honor_tab = (By.ID,u"two2")

    #超市荣誉链接
    honor_link = (By.LINK_TEXT,u"超市荣誉")

    #资质类别
    honor_type = (By.ID,u"uploadFileType")

    #添加按钮
    add_button = (By.CLASS_NAME,u"cxzz_ry_btn")

    #图片选择按钮
    select_file = (By.ID,u"file")

    #描述
    describe = (By.ID,u"oldName")

    #提交
    submit = (By.ID,u"button")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #荣誉总条数
    num = (By.CSS_SELECTOR,u"div.page_yemal p")

