#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#选择地区——省
province = (By.CSS_SELECTOR, "select[onchange='findAreaCode(this,'01')']")

#选择地区——省
city = (By.CSS_SELECTOR, "select[onchange='findAreaCode(this,'02')']")

#选择地区——省
country = (By.CSS_SELECTOR, "select[onchange='findAreaCode(this,'03')']")

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.LINK_TEXT, u"下一页")

