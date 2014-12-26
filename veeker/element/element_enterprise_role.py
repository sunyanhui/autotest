#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementRole(object):

    #角色权限链接
    role_link = (By.LINK_TEXT,u"角色管理")

    #添加角色选项卡
    add_role_tab = (By.ID,u"two2")

    #角色名称
    role_name = (By.ID,u"roleDescribe")

    #超市信息CHECKBOX
    info = (By.NAME,u"all1000")

    #提交
    submit = (By.CSS_SELECTOR,u"input[onclick='submitForm();']")

    #confirm
    confirm = (By.ID,u"popup_ok")

