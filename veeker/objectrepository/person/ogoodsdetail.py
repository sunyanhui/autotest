#!/usr/bin/python2.7
#coding=utf-8
from selenium.webdriver.common.by import By

#***********************找商品***********************#
#找商品
findgood = (By.LINK_TEXT, u'找商品')

#商品名称
goodname = (By.ID, 'goodsName')

#开始价格
startprice = (By.ID, 'promotionPrice')

#结束价格
endprice = (By.ID, 'transacttonPrice')

#所属行业(选择一组，用的时候需要筛选)
selectindustry =(By.CSS_SELECTOR, "a[href^='javascript:findGoodsByIndustryType']")

#搜索按钮
searchButtonForFindgoods = (By.ID, 'button')

#商品链接
goodlink = (By.CSS_SELECTOR, 'td+a+img')

#***********************商品详情***********************#

#商品详情页面
buynow = (By.CSS_SELECTOR, "input[onclick^=shopping]")

#加入到购物车
addtochat = (By.CSS_SELECTOR, "input[onclick^=addShopCart]")

#加入收藏
collect = (By.LINK_TEXT, u"收藏商品")
