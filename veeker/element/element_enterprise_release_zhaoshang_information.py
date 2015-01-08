#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementReleaseZhaoshangInformation(object):

    #发布招商信息链接
    release_zhaoshang_information_link = (By.LINK_TEXT,u"发布招商信息")

    #添加信息TAB页
    add_tab = (By.ID,u"two2")

    #招商级别
    grade = (By.ID,u"grade")

    #合作模式
    mode = (By.XPATH,u"//span[text()='%s']/preceding-sibling::input")

    #招商要求
    require = (By.ID,u"reQuire")

    #备注
    remark = (By.ID,u"memo")

    #保存
    submit = (By.CSS_SELECTOR,u"input[value='保存']")

    #招商信息总数
    num = (By.CSS_SELECTOR,u"div.page_yemal p")

    #确定按钮
    confirm = (By.ID,u"pop_confirm")

