#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementRole(object):

    #角色管理链接
    role_link = (By.LINK_TEXT,u"角色管理")

    #添加角色选项卡
    add_role_tab = (By.XPATH,u"//li[text()='添加角色']")

    #角色名称
    role_name = (By.ID,u"roleDescribe")

    #超市信息CHECKBOX
    info = (By.NAME,u"all120081")

    #提交
    submit = (By.CSS_SELECTOR,u"input[onclick='submitForm();']")

    #confirm
    confirm = (By.ID,u"popup_ok")

