#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementAddOrder(object):

    #添加采购单链接
    add_order_link = (By.LINK_TEXT,u"添加采购单")

    #合作超市下拉框
    supermarket = (By.CLASS_NAME,u"select_showbox")

    #合作超市下拉框列表按索引
    supermarket_index = (By.XPATH,u"//ul[@class='select_option']/li[2]")

    #合作超市下拉框列表按名称
    supermarket_name = (By.XPATH,u"//li[contains(text(),'%s')]")

    #到货日期
    date_arrival = (By.NAME,u"receiveDate")

    #电话
    telephone = (By.ID,u"linkTel")

    #备注
    mark = (By.ID,u"memo")

    #添加明细
    add_list_btn = (By.CSS_SELECTOR,u"input[value='添加明细']")

    #添加明细关闭按钮
    close_btn = (By.CLASS_NAME,u"bu_close")

    #提交按钮
    submit = (By.NAME,u"purchBillSubmit")

    #我的商品
    my_goods = (By.LINK_TEXT,u"我的商品")

