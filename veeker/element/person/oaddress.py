#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#*********************收货地址************************#
#选择省份
province = (By.ID, 'province')

#选择市
city = (By.ID, 'city')

#选择区
country = (By.ID, 'county')

#OK按钮
okButton = (By.ID, 'popup_ok')

#保存提交按钮按钮
Button = (By.ID, 'button')

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