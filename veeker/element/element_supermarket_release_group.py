#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementReleaseGroup(object):

    #发布团购链接
    release_group_link = (By.LINK_TEXT,u"发布团购")

    #商品类别
    goods_type = (By.CLASS_NAME,u"selnews_splb")

    #商品品牌
    goods_brand = (By.CLASS_NAME,u"selnews")

    #商品名称
    goods_name = (By.CLASS_NAME,u"spm_box")

    #商品库存
    goods_stock = (By.NAME,u"goodsDTO.storeNum")

    #商品原价
    original_price = (By.NAME,u"goodsDTO.price")

    #团购价
    group_price = (By.NAME,u"goodsDTO.promotionPrice")

    #起始时间
    start_time = (By.NAME,u"describeDTO.groupStartTime")

    #结束时间
    end_time = (By.NAME,u"describeDTO.groupEndTime")

    #商品描述
    goods_desc = (By.NAME,u"describeDTO.describeName")

    #尺寸
    size = (By.ID,u"val0")

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

