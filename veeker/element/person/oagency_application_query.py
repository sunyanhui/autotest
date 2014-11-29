#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#分销商申请链接
agency_application_query_link = (By.LINK_TEXT, u'分销商申请查询')

#申请日期
start_date = (By.ID, 'startDate')

end_date = (By.ID, 'endDate')

#状态
state = (By.ID, 'state')

#搜索按钮
search_button = (By.ID, 'btnApplyLong btnanniu')

#总条数+总页数 字符串
page_number = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u'下一页')

#OK按钮
okButton = (By.ID, 'popup_ok')