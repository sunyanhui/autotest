#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementReleaseGoods(object):

    #发布商品链接
    release_goods_link = (By.LINK_TEXT,u"发布商品")

    #商品类别
    goods_type = (By.CLASS_NAME,u"selnews_splb")

    #商品品牌
    goods_brand = (By.CLASS_NAME,u"selnews")

    #商品名称
    goods_name = (By.CLASS_NAME,u"spm_box")

    #销售类别
    sale_type = (By.CLASS_NAME,u"xslb_box")

    #商品库存
    goods_stock = (By.NAME,u"goodsDTO.storeNum")

    #使用抵值券
    use_coupon = (By.CSS_SELECTOR,u"input[name='goodsDTO.isCoupon'][vlaue='Y']")

    #不使用抵值券
    not_use_coupon = (By.CSS_SELECTOR,u"input[name='goodsDTO.isCoupon'][vlaue='N']")

    #使用会员折扣
    use_discount = (By.CSS_SELECTOR,u"input[name='goodsDTO.isMemDiscount'][vlaue='Y']")

    #不使用会员折扣
    not_use_discount = (By.CSS_SELECTOR,u"input[name='goodsDTO.isMemDiscount'][vlaue='N']")

    #商品描述
    goods_desc = (By.NAME,u"describeDTO.describeName")

    #价格
    price = (By.CSS_SELECTOR,u"input[name='price'][id='val0']")

    #促销价
    cprice = (By.CSS_SELECTOR,u"input[name='cprice'][id='val1']")

    #采购价
    cgprice = (By.CSS_SELECTOR,u"input[name='cgprice'][id='val1']")

    #选择图片
    select_photo = (By.ID,u"mediaType")

    #点击图片
    photo_for_click = (By.XPATH,u"//div[@id='goodsImage']/div[1]/img")

    #商品描述
    goods_desc_rich = (By.ID,u"myEditor")

    #保存
    save = (By.CLASS_NAME,u"fbsp_serbtn01")

    #保存并上架
    add = (By.CLASS_NAME,u"czsp_serbtn02")

