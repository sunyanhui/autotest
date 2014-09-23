#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#申请分销商链接
apply_agency = (By.LINK_TEXT, u'分销商申请')

#合作模式
mode = (By.ID, 'itemName')

#招商级别
grade = (By.ID, 'gradeId')

#企业名称
company_name = (By.ID, 'enterNameId')

#搜索按钮
search_button = (By.CSS_SELECTOR, "input[onclick='pageSearch(1)']")

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u"下一页")

#OK按钮
okButton = (By.ID, 'popup_ok')

#frame标题
title = (By.CLASS_NAME, 'gy_title')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#对公账号
agency_account = (By.ID, 'agencyAccount')

#开户行
bank = (By.ID, 'bank')

#开户行所在地
bank_address = (By.ID, 'branChBank')

#绑定区域省
bound_province = (By.ID, 'sqbdProvince')

#绑定区域市
bound_city = (By.ID, 'sqbdCity')

#备注
remark = (By.ID, 'mark')

#分销商名称
agency_name = (By.ID, 'agencyName')

#分销商地址
agency_address = (By.ID, 'address')

#学历
education = (By.ID, 'education')

#微信
weixin = (By.ID, 'micro')

#微信二级码
weixin_QR = (By.ID, 'preview1')

#身份证正面
idcard_zm = (By.ID, 'preview2')

#身份证反面
idcard_fm = (By.ID, 'preview3')

#提交按钮
submit = (By.ID, 'sf')





