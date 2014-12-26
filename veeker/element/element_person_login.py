#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementLogin(object):

    #用户名
    username = (By.ID,u"userAccount")

    #密码框1
    password = (By.ID,u"text")

    #密码框2
    password1 = (By.ID,u"userPassword")

    #验证码
    verifycode = (By.ID,u"txtVerifyCode")

    #记住用户名
    rememberuseraccount = (By.ID,u"rememberUserAccount")

    #提交
    submit = (By.CSS_SELECTOR,u"a[href='javascript:login()']")

    #退出登录
    logoutlink = (By.PARTIAL_LINK_TEXT,u"退出")

    #退出确认按钮
    logoutbutton = (By.ID,u"popup_ok")

