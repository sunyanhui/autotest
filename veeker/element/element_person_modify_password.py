#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementModifyPassword(object):

    #账号设置菜单
    account_setting = (By.CSS_SELECTOR,u".setup a")

    #修改密码链接
    modify_password_link = (By.LINK_TEXT,u"修改密码")

    #老密码
    old_password = (By.ID,u"oldPasswordId")

    #新密码
    new_password = (By.NAME,u"userDTO.passWord")

    #重复密码
    repeat_password = (By.NAME,u"repassword")

    #提交按钮
    submit_button = (By.CLASS_NAME,u"tijiaobtn")

