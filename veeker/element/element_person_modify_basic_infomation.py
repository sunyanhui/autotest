#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementModifyBasicInfomation(object):

    #账号设置菜单
    account_setting = (By.CSS_SELECTOR,u".setup a")

    #修改基本信息链接
    modify_basic_information_link = (By.LINK_TEXT,u"基本信息")

    #修改按钮
    modify_button = (By.CSS_SELECTOR,u"input.tijiaobtn.fl")

    #真实姓名
    name = (By.NAME,u"customerPersonDTO.userName")

    #性别男
    sex_boy = (By.ID,u"RadioGroup1_0")

    #性别女
    sex_girl = (By.ID,u"RadioGroup1_1")

    #身份证
    id_card = (By.NAME,u"customerPersonDTO.idCard")

