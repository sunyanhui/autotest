#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementGoodsBrand(object):

    #商品品牌链接
    goods_brand_link = (By.LINK_TEXT,u"商品品牌")

    #添加品牌TAB页
    add_brand_tab = (By.ID,u"two2")

    #选择图片下拉框
    select_img = (By.ID,u"mediaType")

    #点击图片
    photo_for_click = (By.XPATH,u"//div[@id='goodsImage']/div[1]/img")

    #品牌名称
    brand_name = (By.ID,u"brandNames")

    #提交
    submit = (By.ID,u"button")

    #品牌总条数
    num = (By.CSS_SELECTOR,u"div.page_yemal p")

    #品牌删除链接
    del_link = (By.XPATH,u"//td[text()='\n\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40\40%s']/../td[6]/input[2]")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

