# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Chrome()
driver.get("http://www.wiki100.cn")
driver.find_element_by_id("userAccount").clear()
driver.find_element_by_id("userAccount").send_keys("XYHD3100075")
driver.find_element_by_id("text").click()
driver.find_element_by_id("userPassword").clear()
driver.find_element_by_id("userPassword").send_keys("888888")
driver.find_element_by_css_selector("a[href='javascript:login()']").click()
time.sleep(1)
driver.find_element_by_link_text(u"会员等级").click()
driver.switch_to_frame("iframe")
driver.find_element_by_id("modify").click()
print driver.find_element_by_xpath("//td[text()='零售会员']/../td[2]/input").get_attribute("name")