#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementMallHomepage(object):

    #今日订单
    today_order = (By.CSS_SELECTOR,u"div.service_right p b")

    #月订单
    month_order = (By.CSS_SELECTOR,u"div.huiyuan_right span a")

    #切换城市
    change_city = (By.ID,u"changeArea")

    #选择地区
    area = (By.CLASS_NAME,u"weather-city")

    #更换按钮
    change_button = (By.CLASS_NAME,u"gh_btn")

    #登录链接
    login_link = (By.LINK_TEXT,u"登录")

    #注册链接
    regist_link = (By.LINK_TEXT,u"注册")

    #账号输入框
    username = (By.ID,u"userAccount")

    #密码输入框1
    password1 = (By.ID,u"text")

    #密码输入框2
    password2 = (By.ID,u"userPassword")

    #登录按钮
    submit = (By.XPATH,u"//input[@onclick='login()']")

    #商品名输入框
    goods_name_input = (By.CSS_SELECTOR,u"div.search.fl > form > input.text.fl")

    #搜索按钮
    search_button = (By.CSS_SELECTOR,u"div.search.fl > form > input.button.fl")

