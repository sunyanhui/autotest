#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementOrderQuery(object):

    #订单查询链接
    orderQuery = (By.LINK_TEXT,u"订单查询")

    #商品名称
    goodnameforquery = (By.CLASS_NAME,u"spmc_box_text")

    #交易状态
    goodstatus = (By.ID,u"itemName")

    #成交日期-开始
    startsaledate = (By.ID,u"searchbeginDateId")

    #成交日期-结束
    endsaledate = (By.ID,u"searchendDateId")

    #搜索按钮
    searchButtonFororder = (By.NAME,u"cx")

    #订单号码字符串
    stringoforder = (By.CSS_SELECTOR,u"td.order_titlee")

    #总条数+总页数 字符串
    totalpagenumber = (By.CSS_SELECTOR,u"div.page_yemal p")

    #下一页
    nextpage = (By.LINK_TEXT,u"下一页")

    #输入页码
    inputpagenumber = (By.ID,u"go1")

    #GO按钮
    gobutton = (By.LINK_TEXT,u"GO")

    #取消订单
    undoorder = (By.LINK_TEXT,u"取消订单")

    #删除订单
    deleteorder = (By.LINK_TEXT,u"删除")

    #确认收货
    confirmreceipt = (By.CSS_SELECTOR,u"a[href^='javascript:cusOrder.confirmReceiptOrder']")

    #退货原因
    returnreason = (By.ID,u"reasonId")

    #退货说明
    returndescription = (By.NAME,u"replaceGoodsDTO.memo")

    #退货数量
    returnnumber = (By.NAME,u"replaceGoodsDTO.goodsNum")

    #申请退货已发出文字
    returnsucceed = (By.CSS_SELECTOR,u"div.thBox ul li h3")

    #好评
    reviewgrade_01 = (By.CSS_SELECTOR,u"input[value='01']")

    #中评
    reviewgrade_02 = (By.CSS_SELECTOR,u"input[value='02']")

    #差评
    reviewgrade_03 = (By.CSS_SELECTOR,u"input[value='02']")

    #评价内容
    reviewdetail = (By.ID,u"myarea")

    #是否匿名
    ifanonymity = (By.NAME,u"commentDTO.commentType")

    #提示消息
    promptmessage = (By.ID,u"popup_message")

    #购物车链接
    shoppingCart = (By.LINK_TEXT,u"购物车")

    #我的抵值券链接
    myCoupon = (By.LINK_TEXT,u"我的抵值券")

    #企业名称
    entername = (By.ID,u"enterName")

    #有效期-开始
    startDateForCoupon = (By.ID,u"startDate")

    #有效期-结束
    endDateForCoupon = (By.ID,u"endDate")

    #搜索按钮
    searchButtonForCoupon = (By.CLASS_NAME,u"btnApplyLong btnanniu")

    #OK按钮
    okButton = (By.ID,u"popup_ok")

    #保存提交按钮按钮
    Button = (By.ID,u"button")

