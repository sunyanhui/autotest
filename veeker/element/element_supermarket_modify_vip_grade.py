#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementModifyVipGrade(object):

    #会员等级链接
    vip_grade = (By.LINK_TEXT,u"会员等级")

    #修改按钮
    modify = (By.ID,u"modify")

    #零售会员
    lingshou_totalcash = (By.XPATH,u"//td[text()='零售会员']/../td[2]/input")

    #零售会员
    lingshou_discount = (By.XPATH,u"//td[text()='零售会员']/../td[3]/input")

    #零售会员
    lingshou_reason = (By.XPATH,u"//td[text()='零售会员']/../td[4]/input")

    #优惠会员
    youhui_totalcash = (By.XPATH,u"//td[text()='优惠会员']/../td[2]/input")

    #优惠会员
    youhui_discount = (By.XPATH,u"//td[text()='优惠会员']/../td[3]/input")

    #优惠会员
    youhui_reason = (By.XPATH,u"//td[text()='优惠会员']/../td[4]/input")

    #银牌会员
    yinpai_totalcash = (By.XPATH,u"//td[text()='银牌会员']/../td[2]/input")

    #银牌会员
    yinpai_discount = (By.XPATH,u"//td[text()='银牌会员']/../td[3]/input")

    #银牌会员
    yinpai_reason = (By.XPATH,u"//td[text()='银牌会员']/../td[4]/input")

    #金牌会员
    jinpai_totalcash = (By.XPATH,u"//td[text()='金牌会员']/../td[2]/input")

    #金牌会员
    jinpai_discount = (By.XPATH,u"//td[text()='金牌会员']/../td[3]/input")

    #金牌会员
    jinpai_reason = (By.XPATH,u"//td[text()='金牌会员']/../td[4]/input")

    #钻石会员
    zhuanshi_totalcash = (By.XPATH,u"//td[text()='钻石会员']/../td[2]/input")

    #钻石会员
    zhuanshi_discount = (By.XPATH,u"//td[text()='钻石会员']/../td[3]/input")

    #钻石会员
    zhuanshi_reason = (By.XPATH,u"//td[text()='钻石会员']/../td[4]/input")

    #贵宾会员
    guibin_totalcash = (By.XPATH,u"//td[text()='贵宾会员']/../td[2]/input")

    #贵宾会员
    guibin_discount = (By.XPATH,u"//td[text()='贵宾会员']/../td[3]/input")

    #贵宾会员
    guibin_reason = (By.XPATH,u"//td[text()='贵宾会员']/../td[4]/input")

    #保存
    submit = (By.ID,u"confirm")

