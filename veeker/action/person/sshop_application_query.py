#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.person.oshop_application_query import *
from common import output, common
from action.basepage import BasePage
from selenium.webdriver.support.select import Select

class ShopApplicationQuery(BasePage):

    def search(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element


        try:
            sdriver(*shop_application_query).click()
            driver.switch_to_frame('iframe')
            sdriver(*start_date).send_keys(w['startdate'])
            sdriver(*end_date).send_keys(w['enddate'])
            Select(sdriver(*state)).select_by_visible_text(w['state'])
            sdriver(*search_button).click()
            page = common.get_orderpage(sdriver(*page_number).text)
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'search pass~!', pagelist=page)
        finally:
            driver.switch_to_default_content()
