#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementIntroduction(object):

    #简介链接
    introduction_link = (By.LINK_TEXT,u"企业简介")

    #介绍选项卡
    introduction = (By.ID,u"two1")

    #文件选项卡
    culture = (By.ID,u"two2")

    #组织结构选项卡
    structure = (By.ID,u"two3")

    #简介富文本编辑框
    introduction_rich_text = (By.ID,u"enterIntroClob")

    #文件富文本编辑框
    culture_rich_text = (By.ID,u"enterCultureClob")

    #组织结构富文本编辑框
    structure_rich_text = (By.ID,u"structureIdClob")

    #简介提交按钮
    introduction_button = (By.XPATH,u"//div[@id='con_two_1']/div[2]/input")

    #企业文件提交按钮
    culture_button = (By.XPATH,u"//div[@id='con_two_2']/div[2]/input")

    #组织架构提交按钮
    structure_button = (By.XPATH,u"//div[@id='con_two_3']/div[2]/input")

    #确认按钮
    confirm = (By.ID,u"popup_ok")

