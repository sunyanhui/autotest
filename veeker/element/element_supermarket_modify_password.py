#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementModifyPassword(object):

    #修改密码链接
    modify_passwork_link = (By.LINK_TEXT,u"密码修改")

    #旧密码
    old_password = (By.NAME,u"oldPassword")

    #新密码
    new_password = (By.NAME,u"userDTO.userPassword")

    #密码确认
    repeat_password = (By.NAME,u"repassword")

    #提交
    submit = (By.CLASS_NAME,u"btn_tjmm")

