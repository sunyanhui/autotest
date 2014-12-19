#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

#角色权限链接
role_link = (By.LINK_TEXT, u'角色权限')

#添加角色选项卡
add_role = (By.ID, 'two2')

#角色名称
role_name = (By.ID, 'roleDescribe')

#超市信息CHECKBOX
info = (By.NAME, 'all120034')

#提交
submit = (By.CSS_SELECTOR, "input[onclick='submitForm();']")

#confirm
confirm = (By.ID, "popup_ok")