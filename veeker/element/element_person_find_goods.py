#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementFindGoods(object):

    #找商品
    findgood = (By.LINK_TEXT,u"找商品")

    #商品名称
    goodname = (By.ID,u"goodsName")

    #开始价格
    startprice = (By.ID,u"promotionPrice")

    #结束价格
    endprice = (By.ID,u"transacttonPrice")

    #所属行业(选择一组，用的时候需要筛选)
    selectindustry = (By.CSS_SELECTOR,u"a[href^='javascript:findGoodsByIndustryType']")

    #搜索按钮
    searchButtonForFindgoods = (By.ID,u"button")

    #总条数+总页数 字符串
    totalpagenumber = (By.CSS_SELECTOR,u"div.page_yemal p")

    #商品链接
    goodlink = (By.CSS_SELECTOR,u"td+a+img")

    #下一页
    nextpage = (By.LINK_TEXT,u"下一页")

