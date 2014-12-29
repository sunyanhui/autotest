#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

#管理员权限链接
manager_link = (By.LINK_TEXT, u'操作员管理')

#添加管理员选项卡
add_manager = (By.ID, 'two2')

#管理员账号
manager_account = (By.ID, 'userAccount')

#管理员权限
manager_role = (By.ID, 'roleId')

#提交
submit = (By.CSS_SELECTOR, "input[onclick='submitForm();']")

#confirm
confirm = (By.ID, "popup_ok")