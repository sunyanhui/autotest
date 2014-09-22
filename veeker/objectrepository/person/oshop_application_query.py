#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#开店申请查询
shop_application_query = (By.LINK_TEXT, u'开店申请查询')

#申请日期
start_date = (By.ID, 'startDate')
end_date = (By.ID, 'endDate')

#状态
state = (By.ID, 'state')

#搜索按钮
search_button = (By.ID, 'btnApplyLong btnanniu')

