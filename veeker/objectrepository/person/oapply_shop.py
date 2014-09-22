#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#开店申请链接
applyshop = (By.LINK_TEXT, u'开店申请')
#预订产品
product = (By.ID, 'productCode')
#经营类型
type = (By.ID, 'operateType')
#合作省
province_hezuo = (By.ID, 'cooperateProvince')
#合作市
city_hezuo = (By.ID, 'cooperateCity')
#合作县
country_hezuo = (By.ID, 'cooperateArea')
#企业名称
entername = (By.ID, 'enterName')
#联系人
linkman = (By.ID, 'linkMan')
#联系电话
phone = (By.ID, 'linkWay')
#微信
weixin = (By.ID, 'micro')
#QQ号
qq = (By.ID, 'qq')
#邮箱
email = (By.ID, 'email')
#区域省
province_region = (By.ID, 'belongProvince')
#区域市
city_region = (By.ID, 'belongCity')
#区域县
country_region = (By.ID, 'belongArea')
#详细地址
address = (By.ID, 'address')
#备注
remark = (By.ID, 'memo')
#保存按钮
submit = (By.CLASS_NAME, 'shop_back')
#frame标题
title = (By.CLASS_NAME, 'gy_title')

