#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementPictureSpace(object):

    #图片空间链接
    picture_space_link = (By.LINK_TEXT,u"图片空间")

    #图片上传链接
    upload_link = (By.LINK_TEXT,u"图片上传")

    #添加图片按钮
    add_picture_button = (By.ID,u"SWFUpload_0")

    #图片上传按钮
    upload_button = (By.ID,u"btnUpload")

    #图片删除链接
    del_link = (By.XPATH,u"//p[text()='%s']/../table//a[text()='删除']")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #回收站图片链接
    recycle_link = (By.LINK_TEXT,u"回收站图片")

    #清空链接
    empty_link = (By.LINK_TEXT,u"清空")

