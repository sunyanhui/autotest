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

#总条数+总页数 字符串
totalpagenumber = (By.CSS_SELECTOR, 'div.page_yemal p')

#商品链接
goodlink = (By.CSS_SELECTOR, 'td+a+img')

#下一页
nextpage = (By.LINK_TEXT, u"下一页")

#***********************商品详情***********************#

#商品规格
goodsoption = (By.CSS_SELECTOR, "a[onclick^='argument1(this']")

#商品数量
goodsnum = (By.ID, 'goodsNum')

#立即购买
buynow = (By.CSS_SELECTOR, "input[onclick^=shopping]")

#加入到购物车
addtochat = (By.CSS_SELECTOR, "input[onclick^=addShopCart]")

#去购物车结算
gotosettle = (By.CSS_SELECTOR, "input[onclick^='goAccounts']")

#加入收藏
collect = (By.LINK_TEXT, u"收藏商品")

#*****************第一次新增收货地址的表单*****************#

nulladressform = (By.ID, "AddNullReciveAdress")

#第一次新增——省市县
province_null = (By.ID, 'province')
city_null = (By.ID, 'addNuCity')
country_null = (By.ID, 'addNuCounty')

#详细地址
detailaddress = (By.NAME, 'receiveAddDTO.addDetail')

#邮政编码
zipcode = (By.NAME, 'receiveAddDTO.zipCode')

#收货人
receivename = (By.NAME, 'receiveAddDTO.revicerName')

#手机号码
mobilenumber = (By.NAME, 'receiveAddDTO.mobile')

#电话号码
telephonenumber = (By.NAME, 'receiveAddDTO.telPhone')

#是否设为默认收货地址
ifdefaultaddress = (By.NAME, 'receiveAddDTO.isDefault')

#第一次新增按钮
button_null = (By.ID, 'addButton')

#有了再新增
addreciveadress = (By.ID, 'AddReciveAdress')

#编辑收货地址
updatereciveadress_null = (By.ID, 'updateReciveAdress')

#***********************订单结算页面***********************#

#是否开发票
invoice_yes = (By.CSS_SELECTOR, "input[value='01'][name='orderDTO.isNeedInvoice']")
invoice_no = (By.CSS_SELECTOR, "input[value='02'][name='orderDTO.isNeedInvoice']")

#发票抬头
invoice_title = (By.ID, 'invoiceChequeTextId')

#备注
remark = (By.ID, 'mallmemoid')

#结算方式贷到付款
payondelivery = (By.CSS_SELECTOR, "input[value='02'][name='orderDTO.payKind']")

#使用抵值券
usecoupon = (By.CSS_SELECTOR, "input[onclick='showCusCoupon('cusCouponListId');']")

#提交订单
submitorder = (By.CSS_SELECTOR, "input[onclick='submitOrders()']")

#订单号码
ordernumber = (By.XPATH, "//div[@id='wraper']/div/div[1]/p/b[1]")