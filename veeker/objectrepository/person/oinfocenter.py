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

#*********************基本信息************************#
#基本信息链接
basicinFormation = (By.LINK_TEXT, u'基本信息')

#真实姓名
realname = (By.ID, 'personName')

#姓别选项
sexboy = (By.ID, 'RadioGroup1_0')

#性别选项
sexgirl = (By.ID, 'RadioGroup1_1')

#身份证号
idcard = (By.ID, 'idCard')

#手机号
telephoneForMdInfo = (By.ID, 'telephone')

#生日选项
birthdayForMdInfo = (By.ID, 'birthday')

#详细地址
addressForMdInfo = (By.ID, 'address')

#*********************收货地址************************#
#收货地址
shoppingAddress = (By.LINK_TEXT, u'收货地址')

#详细地址
addressForMdAd = (By.NAME, 'receiveAddDTO.addDetail')

#邮政编码
zipCodeForMdAd = (By.NAME, 'receiveAddDTO.zipCode')

#收货人
revicerNameForMdAd = (By.NAME, 'receiveAddDTO.revicerName')

#手机号码
mobileForMdAd = (By.NAME, 'receiveAddDTO.mobile')

#电话号码
telephoneForMdAd = (By.NAME, 'receiveAddDTO.telPhone')

#设为默认收货地址
isDefaultAddress = (By.NAME, 'receiveAddDTO.isDefault')

#已保存地址数
addressNumber = (By.CSS_SELECTOR, 'body p span')

#修改收货地址链接
mdaddressLink = (By.LINK_TEXT, u'修改')

#删除收货地址链接
deladdressLink = (By.LINK_TEXT, u'删除')