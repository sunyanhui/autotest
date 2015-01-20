#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementApplyShop(object):

    #联盟店申请链接
    apply_shop_link = (By.LINK_TEXT,u"联盟店申请")

    #合作模式
    mode = (By.ID,u"itemName")

    #超市名称
    supermarket_name = (By.ID,u"enterNameId")

    #搜索按钮
    search = (By.CSS_SELECTOR,u"input[value='搜索']")

    #申请按钮
    apply_btn = (By.CSS_SELECTOR,u"input[value='申请']")

    #对公账号
    account = (By.ID,u"agencyAccount")

    #银行
    bank = (By.ID,u"bank")

    #银行所在地
    bank_location = (By.ID,u"branChBank")

    #绑定街道
    binding_street = (By.ID,u"sqbdProvince")

    #绑定社区
    binding_community = (By.ID,u"sqbdCity")

    #店铺街道
    shop_street = (By.ID,u"sqbdProvince2")

    #店铺社区
    shop_community = (By.ID,u"storeAreaCode")

    #店铺详细地址
    shop_detail_address = (By.ID,u"storeAddress")

    #备注
    remark = (By.ID,u"mark")

    #店铺名称
    shop_name = (By.ID,u"agencyName")

    #店铺地址
    shop_address = (By.ID,u"address")

    #学历
    education = (By.ID,u"education")

    #微信
    weixin = (By.ID,u"micro")

    #二维码
    or_code = (By.ID,u"ewm")

    #身份证正面
    id_zm = (By.ID,u"zm")

    #身份证反面
    id_fm = (By.ID,u"fm")

    #提交
    submit = (By.ID,u"sf")

