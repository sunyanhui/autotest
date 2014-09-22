#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#被诉单位
compaintcompany = (By.ID, 'byComplaintCompanyId')

#流程
flow = (By.ID, 'flow')

#被诉日期
startdate = (By.ID, 'startDate')
enddate = (By.ID, 'endDate')

#状态
state = (By.ID, 'flowState')

#搜索按钮
searchbutton = (By.ID, 'btnApplyLong btnanniu')