#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from element.person.omy_complaint import *
from action.basepage import BasePage
from common import output, common
import time

class MyComplaint(BasePage):

    def search(self, **w):
        driver = self.driver
        driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*my_complaint).click()
            driver.switch_to_frame('iframe')
            sdriver(*compaint_company).send_keys(w['compaint_company'])
            Select(sdriver(*flow)).select_by_visible_text(w['flow'])
            sdriver(*start_date).send_keys(w['start_date'])
            sdriver(*end_date).send_keys(w['end_date'])
            Select(sdriver(*state)).select_by_visible_text(w['state'])
            sdriver(*search_button).click()
            page = common.get_orderpage(sdriver(*page_number).text)
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'search pass~!', pagelist=page)
        finally:
            driver.switch_to_default_content()