#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
from element.person.oagency_application_query import *
from common import output, common_method
from action.basepage import BasePage


class AgencyApplicationQuery(BasePage):

    def search(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element


        try:
            sdriver(*agency_application_query_link).click()
            driver.switch_to_frame('iframe')
            sdriver(*start_date).send_keys(w['startdate'])
            sdriver(*end_date).send_keys(w['enddate'])
            Select(sdriver(*state)).select_by_visible_text(w['state'])
            sdriver(*search_button).click()
            page = common_method.get_orderpage(sdriver(*page_number).text)
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'search pass~!', pagelist=page)
        finally:
            driver.switch_to_default_content()



