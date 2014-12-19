#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

modify_passwork_link = (By.LINK_TEXT, u'密码修改')
old_password = (By.NAME, 'oldPassword')
new_password = (By.NAME, 'userDTO.userPassword')
repeat_password = (By.NAME, 'repassword')
submit = (By.CLASS_NAME, 'btn_tjmm')