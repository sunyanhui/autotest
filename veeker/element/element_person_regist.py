#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementRegist(object):

    #注册链接
    registerlink = (By.LINK_TEXT,u"免费注册")

    #选择省
    province = (By.ID,u"provinceAreaCode")

    #选择市
    city = (By.ID,u"citycode")

    #选择地区错误提示
    areaprompt = (By.ID,u"checkProvinceAreaCode")

    #昵称
    nickname = (By.ID,u"nickName")

    #密码
    password = (By.ID,u"passWord")

    #密码确认
    confirmpassword = (By.ID,u"userPasswordComfirm")

    #协议确认选项框
    checkbox = (By.CLASS_NAME,u"check_tb")

    #邮箱注册链接
    registerbutton = (By.LINK_TEXT,u"邮箱注册")

    #邮件地址
    email = (By.ID,u"email")

    #验证码输入框
    emailcode = (By.ID,u"emailCode")

    #获取验证码按钮
    getmailcode = (By.ID,u"button")

    #提交
    submit = (By.LINK_TEXT,u"提交")

    #忘记密码链接
    forgotPassword = (By.LINK_TEXT,u"忘记登录密码？")

    #用户名输入框
    userAccount = (By.ID,u"userAccount")

    #验证码输入框
    emailCodeForFind = (By.NAME,u"emailCode")

    #下一步按钮
    nextstep = (By.ID,u"submitButton")

    #返回登录
    bact_login = (By.LINK_TEXT,u"返回登录")

    #订单号码
    orderNumber = (By.XPATH,u"/html/body/div[3]/div[3]/div/p[1]")

