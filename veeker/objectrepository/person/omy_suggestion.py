#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#被建议单位单位
suggestioncompany = (By.ID, 'companyId')

#状态
state = (By.ID, 'flowState')

#被诉日期
startdate = (By.ID, 'startDate')
enddate = (By.ID, 'endDate')

#搜索按钮
searchbutton = (By.ID, 'btnApplyLong btnanniu')