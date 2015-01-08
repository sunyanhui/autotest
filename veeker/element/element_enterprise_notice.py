#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementNotice(object):

    #公告标题
    title = (By.ID,u"title")

    #公告内容
    content = (By.CLASS_NAME,u"tzgg_content")

    #发布
    publish = (By.ID,u"publishs")

    #提交
    submit = (By.CSS_SELECTOR,u"input[type='submit']")

    #返回按钮
    back = (By.CSS_SELECTOR,u"input[value='返回']")

    #删除链接
    del_link = (By.XPATH,u"//a[text()='%s']/../../td[6]/input[2]")

    #通知公告管理
    notice_manage_link = (By.LINK_TEXT,u"通知公告")

    #添加公告TAB页
    add_notice_tab = (By.ID,u"two2")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #公告总数
    num = (By.CSS_SELECTOR,u"div.page_yemal p")

