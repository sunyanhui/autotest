#-*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# a = u"首页上一页12 3 4 下一页末页共4页 , 共36条    跳到至 页 确定"
# print re.search(u"共(\d*)条",a).group(1)


# driver = webdriver.Chrome()
# driver.get("http://tieba.baidu.com/f/search/adv")
# driver.find_element_by_name("kw").send_keys("test")
# driver.find_element_by_xpath(u"//input[@value='贴吧搜索']").click()
# time.sleep(3)
# driver.quit()

# driver.get("http://www.wiki100.cn")
# driver.find_element_by_id("userAccount").clear()
# driver.find_element_by_id("userAccount").send_keys("XYHD3100075")
# driver.find_element_by_id("text").click()
# driver.find_element_by_id("userPassword").clear()
# driver.find_element_by_id("userPassword").send_keys("888888")
# driver.find_element_by_css_selector("a[href='javascript:login()']").click()
# time.sleep(1)
# # driver.find_element_by_link_text(u"会员等级").click()
# # driver.switch_to_frame("iframe")
# # driver.find_element_by_id("modify").click()
# # print driver.find_element_by_xpath("//td[text()='零售会员']/../td[2]/input").get_attribute("name")
#
# driver.find_element_by_link_text(u"超市简介").click)
# driver.switch_to_frame("iframe")
# JS = "UE.getEditor('enterIntroClob').execCommand('inserthtml','<b>123</b>');"
# driver.execute_script(JS)
#
# driver.switch_to_default_content()
# driver.find_element_by_css_selector()
# driver.implicitly_wait()

# driver.switch_to.frame()
# driver.switch_to.default_content()
#
# #!/usr/bin/env python
# #coding=utf-8
# from selenium import webdriver
# import logging
#
# logging.BASIC_FORMAT()
# d = webdriver.Chrome()
# print "`"*30
# d.get("http://www.baidu.com")
# print "`"*30
# d.quit()
from flask import Flask
a = Flask(__name__)
a.config