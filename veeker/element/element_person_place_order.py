#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementPlaceOrder(object):

    #普通商品详情----商品规格
    goodsoption = (By.CSS_SELECTOR,u"a[onclick^='argument1(this']")

    #商品数量
    goodsnum = (By.ID,u"goodsNum")

    #立即购买
    buynow = (By.CSS_SELECTOR,u"input[onclick^=shopping]")

    #加入到购物车
    addtochat = (By.CSS_SELECTOR,u"input[onclick^=addShopCart]")

    #去购物车结算
    gotosettle = (By.CSS_SELECTOR,u"input[onclick^='goAccounts']")

    #加入收藏
    collect = (By.LINK_TEXT,u"收藏商品")

    #团购商品详情---马上团
    groupnow = (By.CSS_SELECTOR,u"input[onclick='xianshi()']")

    #选择类型
    select_class = (By.CSS_SELECTOR,u"input[type='checkbox']")

    #确定
    confirm = (By.CSS_SELECTOR,u"input[onclick='buying()']")

    #第一次新增收货地址的表单
    nulladressform = (By.ID,u"AddNullReciveAdress")

    #省
    province_null = (By.ID,u"area")

    #市
    city_null = (By.ID,u"addNuCity")

    #县
    country_null = (By.ID,u"addNuCounty")

    #详细地址
    detailaddress = (By.NAME,u"receiveAddDTO.addDetail")

    #邮政编码
    zipcode = (By.NAME,u"receiveAddDTO.zipCode")

    #收货人
    receivename = (By.NAME,u"receiveAddDTO.revicerName")

    #手机号码
    mobilenumber = (By.NAME,u"receiveAddDTO.mobile")

    #电话号码
    telephonenumber = (By.NAME,u"receiveAddDTO.telPhone")

    #是否设为默认收货地址
    ifdefaultaddress = (By.NAME,u"receiveAddDTO.isDefault")

    #第一次新增按钮
    button_null = (By.ID,u"addButton")

    #有了再新增
    addreciveadress = (By.ID,u"AddReciveAdress")

    #编辑收货地址
    updatereciveadress_null = (By.ID,u"updateReciveAdress")

    #订单结算页面---商品总价
    total_price = (By.NAME,u"price")

    #应付总额
    should_pay_price = (By.ID,u"J_ActualFee")

    #开发票
    invoice_yes = (By.CSS_SELECTOR,u"input[value='01'][name='orderDTO.isNeedInvoice']")

    #不开发票
    invoice_no = (By.CSS_SELECTOR,u"input[value='02'][name='orderDTO.isNeedInvoice']")

    #发票抬头
    invoice_title = (By.ID,u"invoiceChequeTextId")

    #备注
    remark = (By.ID,u"mallmemoid")

    #结算方式贷到付款
    payondelivery = (By.CSS_SELECTOR,u"input[value='02'][name='orderDTO.payKind']")

    #使用抵值券
    usecoupon = (By.CSS_SELECTOR,u"input[onclick='showCusCoupon('cusCouponListId');']")

    #提交订单
    submitorder = (By.CSS_SELECTOR,u"input[onclick='submitOrders()']")

    #订单号码
    ordernumber = (By.XPATH,u"//div[@class='ordersuccess']/p/b[1]")

