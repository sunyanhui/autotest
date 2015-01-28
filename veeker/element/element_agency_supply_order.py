#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementSupplyOrder(object):

    #企业下拉框
    enterprise = (By.CSS_SELECTOR,u"div#enterId div")

    #企业下拉框列表按索引
    enterprise_index = (By.XPATH,u"//ul[@class='select_option']/li[2]")

    #企业下拉框列表按名称
    enterprise_name = (By.XPATH,u"//li[contains(text(),'%s')]")

    #申请日期-开始
    date_start = (By.NAME,u"purchBillDTO.flowDateBegin")

    #申请日期-结束
    date_end = (By.NAME,u"purchBillDTO.flowDateEnd")

    #订单状态
    order_status = (By.CSS_SELECTOR,u"div#auditState div")

    #企业供货订单
    supply_order_link = (By.LINK_TEXT,u"企业供货订单")

    #订单数量
    order_num = (By.CLASS_NAME,u"pagelist")

    #未发布
    unpublished = (By.CSS_SELECTOR,u"ul.select_option li[val='01']")

    #确定按钮
    ok_btn = (By.ID,u"popup_ok")

