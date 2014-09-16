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
nextpage = (By.LINK_TEXT, u"下一页")

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

#***********************申请退货***********************#

#退货原因
returnreason = (By.ID, 'reasonId')

#退货说明
returndescription = (By.NAME, 'replaceGoodsDTO.memo')

#退货数量
returnnumber = (By.NAME, 'replaceGoodsDTO.goodsNum')

#申请退货已发出文字
returnsucceed = (By.CSS_SELECTOR, "div.thBox ul li h3")

#***********************评价链接***********************#

#评价等级（01：好评， 02：中评， 03差评）
reviewgrade_01 = (By.CSS_SELECTOR, "input[value='01']")
reviewgrade_02 = (By.CSS_SELECTOR, "input[value='02']")
reviewgrade_03 = (By.CSS_SELECTOR, "input[value='03']")

#评价内容
reviewdetail = (By.ID, 'myarea')

#是否匿名
ifanonymity = (By.NAME, 'commentDTO.commentType')

#提示消息
promptmessage = (By.ID, 'popup_message')

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
