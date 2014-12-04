#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#基本信息链接
basicinfo = (By.LINK_TEXT, u'基本信息')

#真实姓名
realname = (By.ID, 'personName')

#姓别选项
sexboy = (By.ID, 'RadioGroup1_0')

#性别选项
sexgirl = (By.ID, 'RadioGroup1_1')

#身份证号
idcard = (By.ID, 'idCard')

#手机号
telephone = (By.ID, 'telephone')

#生日选项
birthday = (By.ID, 'birthday')

#详细地址
address = (By.ID, 'address')

#选择省份
province = (By.ID, 'area')

#选择市
city = (By.ID, 'city')

#选择区
country = (By.ID, 'county')

#OK按钮
okButton = (By.ID, 'popup_ok')

#保存提交按钮按钮
Button = (By.ID, 'button')