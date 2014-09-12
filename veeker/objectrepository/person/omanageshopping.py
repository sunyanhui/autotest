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

#订单号码字符串
stringoforder = (By.CSS_SELECTOR, 'td.order_titlee')

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#下一页
nextpage = (By.CSS_SELECTOR, 'a.page_a u:contains('+u'下一页'+')')

#输入页码
inputpagenumber = (By.ID, 'go1')

#GO按钮
gobutton = (By.LINK_TEXT, 'GO')

#取消订单
undoorder = (By.LINK_TEXT, u'取消订单')

#删除订单
deleteorder = (By.LINK_TEXT, u'删除')

#确认收货
confirmreceipt = (By.CSS_SELECTOR, "a[href^='javascript:cusOrder.confirmReceiptOrder']")

#退货链接
applyreturn =(By.CSS_SELECTOR, "a[href^='javascript:cusOrder.applyRefund']")

#退货原因
returnreason = (By.ID, 'reasonId')

#退货说明
returndescription = (By.NAME, 'replaceGoodsDTO.memo')

#退货数量
returnnumber = (By.NAME, 'replaceGoodsDTO.goodsNum')

#申请退货已发出
returnsuccee = (By.CSS_SELECTOR, u"h3:contains('申请退货已发出')")

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
