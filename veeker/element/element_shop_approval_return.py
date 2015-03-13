#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementApprovalReturn(object):

    #退货商品审批链接
    approval_return_link = (By.LINK_TEXT,u"退货商品审批")

    #审批通过
    approval_by = (By.CSS_SELECTOR,u"input[name='replaceGoodsDto.auditState'][value='02']")

    #审批驳回
    approval_turn_down = (By.CSS_SELECTOR,u"input[name='replaceGoodsDto.auditState'][value='03']")

    #审批意见
    approval_comments = (By.ID,u"approval_opinion")

    #提交
    submit = (By.CLASS_NAME,u"tijiaobg")

