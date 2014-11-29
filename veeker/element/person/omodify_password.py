#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


#***********************密码修改***********************#
#密码修改链接
modifyPassword = (By.LINK_TEXT, u"密码修改")

#原密码输入框
oldPasswordInput = (By.ID, 'oldPasswordId')

#新密码输入框
newPasswordInput = (By.NAME, 'userDTO.userPassword')

#确认密码输入框
confirmPasswordInput = (By.NAME, 'repassword')

#密码修改提交按钮
passwordSubmit = (By.ID, 'button')

#修改后提示
passMessage = (By.ID, 'popup_message')