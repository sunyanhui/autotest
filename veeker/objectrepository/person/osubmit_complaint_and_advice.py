#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

#建议投诉链接
complaint_and_advice = (By.LINK_TEXT, u'投诉建议')

#发表投诉链接
submit_complaint_link = (By.LINK_TEXT, u'发表投诉')

#发表建议链接
submit_advice = (By.LINK_TEXT, u'发表建议')

#投诉对象——企业
complaint_company = (By.CSS_SELECTOR, "input[name='complaintDTO.suggestobject'][value='1']")

#投诉对象——分销商
complaint_agency = (By.CSS_SELECTOR, "input[name='complaintDTO.suggestobject'][value='2']")

#投诉商品
complaint_goods = (By.CSS_SELECTOR, "input[name='complaintDTO.complaintType'][value='1']")

#投诉客服
complaint_service = (By.CSS_SELECTOR, "input[name='complaintDTO.complaintType'][value='2']")

#投诉标题
complaint_title = (By.CSS_SELECTOR, "input[name='complaintDTO.complaintTitle']")

#投诉内容
complaint_detail = (By.CSS_SELECTOR, "input[name='complaintDTO.complaintContent']")

#建议企业
suggest_company = (By.CSS_SELECTOR, "input[name='proposalDTO.suggestobject'][value='1']")

#建议分销商
suggest_agency = (By.CSS_SELECTOR, "input[name='proposalDTO.suggestobject'][value='2']")

#建议商品
suggest_goods = (By.CSS_SELECTOR, "input[name='proposalDTO.type'][value='1']")

#建议服务
suggest_service = (By.CSS_SELECTOR, "input[name='proposalDTO.type'][value='2']")

#建议标题
suggest_title = (By.CSS_SELECTOR, "input[name='proposalDTO.title']")

#建议内容
suggest_detail = (By.CSS_SELECTOR, "input[name='proposalDTO.content']")

#提交
submit = (By.CLASS_NAME, "complain_btn")

#结果提示DIV
prompt = (By.ID, 'promptInfo')