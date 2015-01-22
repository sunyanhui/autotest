#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementBusinessCooperation(object):

    #合作商家链接
    business_cooperation_link = (By.LINK_TEXT,u"合作商家")

    #联盟企业输入框
    alliance_enterprise_input = (By.ID,u"enterName")

    #联盟状态
    alliance_status = (By.CLASS_NAME,u"select_showbox")

    #搜索
    search_button = (By.CLASS_NAME,u"searchbtn")

    #联盟状态下拉列表
    alliance_status_list = (By.CSS_SELECTOR,u"ul.select_option li")

