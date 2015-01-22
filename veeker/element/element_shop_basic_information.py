#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementBasicInformation(object):

    #手机号码
    telephone = (By.ID,u"telephone")

    #微信
    weixin = (By.ID,u"personDTO.micro")

    #开户行
    opening_bank_input = (By.CLASS_NAME,u"select_showbox")

    #开户行下拉列表
    opening_bank_list = (By.CSS_SELECTOR,u"ul.select_option li")

    #开户行所在地
    opening_bank_location = (By.ID,u"branChBank")

    #对公账号
    agency_account = (By.ID,u"agencyAccount")

    #微信二维码
    weixin_or = (By.ID,u"erweima")

    #基本信息链接
    basic_information_link = (By.LINK_TEXT,u"基本信息")

    #错误提示信息
    error_infomation = (By.CLASS_NAME,u"Validform_wrong")

    #基本信息表头
    form_head = (By.CLASS_NAME,u"right_title")

    #修改按钮
    submit = (By.CLASS_NAME,u"xiugaibg")

    #开户行下拉列表
    opening_bank_list2 = (By.XPATH,u"//li[text()=' %s']")

