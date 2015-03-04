#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementGoodsBought(object):

    #已买到的商品链接
    goods_bought_link = (By.LINK_TEXT,u"已买到的商品")

    #退货原因选择框
    return_reason_input = (By.CLASS_NAME,u"width230")

    #退货原因选项
    return_reason_select = (By.XPATH,u"//li[text()='%s']")

    #退货说明
    return_describe = (By.NAME,u"replaceGoodsDTO.memo")

    #退货数量
    return_number = (By.NAME,u"replaceGoodsDTO.goodsNum")

    #凭证1
    return_proof = (By.ID,u"preview1")

    #提交
    submit = (By.CSS_SELECTOR,u".tijiaobtn.fl")

