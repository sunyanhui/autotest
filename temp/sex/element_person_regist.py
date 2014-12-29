#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementRegist(object):

    #
    registerlink = (By.LINK_TEXT,u"免费注册")

    #
    province = (By.ID,u"provinceAreaCode")

    #
    city = (By.ID,u"citycode")

    #
    areaprompt = (By.ID,u"checkProvinceAreaCode")

    #
    nickname = (By.ID,u"nickName")

    #
    password = (By.ID,u"userPassword")

    #
    confirmpassword = (By.ID,u"userPasswordComfirm")

    #
    checkbox = (By.CLASS_NAME,u"check_tb")

    #
    registerbutton = (By.LINK_TEXT,u"邮箱注册")

    #
    email = (By.ID,u"email")

    #
    emailcode = (By.ID,u"emailCode")

    #
    getmailcode = (By.ID,u"button")

    #
    submit = (By.LINK_TEXT,u"提交")

    #
    forgotPassword = (By.LINK_TEXT,u"忘记登录密码？")

    #
    userAccount = (By.ID,u"userAccount")

    #
    emailCodeForFind = (By.NAME,u"emailCode")

    #
    nextstep = (By.ID,u"submitButton")

    #
    bact_login = (By.LINK_TEXT,u"返回登录")

    #
    orderNumber = (By.XPATH,u"/html/body/div[3]/div[3]/div/p[1]")

