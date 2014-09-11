#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#***********************订单查询***********************#
#订单查询链接
orderQuery = (By.LINK_TEXT, u'订单查询')

#商品名称
goodnameforquery = (By.CLASS_NAME, 'spmc_box_text')

#交易状态
goodstatus = (By.ID, 'itemName')

#成交日期
startsaledate = (By.ID, 'searchbeginDateId')
endsaledate = (By.ID, 'searchendDateId')

#搜索按钮
searchButtonFororder = (By.NAME, 'cx')

#订单总数字串
stringoforder = (By.CSS_SELECTOR, 'td.order_titlee')

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.CSS_SELECTOR, 'a.page_a u')

#***********************找商品***********************#
#找商品
findgood = (By.LINK_TEXT, u'找商品')

#商品名称
goodname = (By.ID, 'goodsName')

#开始价格
startprice = (By.ID, 'promotionPrice')

#结束价格
endprice = (By.ID, 'transacttonPrice')

#搜索按钮
searchButtonForFindgoods = (By.ID, 'button')

#商品链接
goodlink = (By.CSS_SELECTOR, 'td+a+img')

#***********************我的收藏***********************#
#我的收藏链接
myFavorites = (By.LINK_TEXT, u'我的收藏')


#************************购物车************************#
#购物车链接
shoppingCart = (By.LINK_TEXT, u'购物车')


#************************抵值券************************#
#我的抵值券链接
myCoupon = (By.LINK_TEXT, u'我的抵值券')

#企业名称
entername = (By.ID, 'enterName')

#有效期选择
startDateForCoupon = (By.ID, 'startDate')
endDateForCoupon = (By.ID, 'endDate')

#状态
stateForCoupon = (By.ID, 'state', "//option[@value='01']")

#搜索按钮
searchButtonForCoupon = (By.CLASS_NAME, 'btnApplyLong btnanniu')
