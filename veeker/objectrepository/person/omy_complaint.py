#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#我的投诉链接
my_complaint = (By.LINK_TEXT, u'我的投诉')

#被诉单位
compaint_company = (By.ID, 'byComplaintCompanyId')

#流程
flow = (By.ID, 'flow')

#被诉日期
start_date = (By.ID, 'startDate')

end_date = (By.ID, 'endDate')

#状态
state = (By.ID, 'flowState')

#搜索按钮
search_button = (By.ID, 'btnApplyLong btnanniu')

#总条数+总页数 字符串
page_number = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u'下一页')

#OK按钮
okButton = (By.ID, 'popup_ok')