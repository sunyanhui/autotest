#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#申请分销商链接
apply_distributor = (By.LINK_TEXT, u'分销商申请')

#合作模式
mode = (By.ID, 'itemName')

#招商级别
grade = (By.ID, 'gradeId')

#企业名称
company_name = (By.ID, 'enterNameId')

#搜索按钮
search_button = (By.CLASS_NAME, 'btnApplyLong btnanniu')

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u"下一页")