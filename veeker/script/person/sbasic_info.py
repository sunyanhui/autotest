#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from objectrepository.person.obasic_info import *
from framework import output
from script.sbase import Base
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import re

class Basic_Info(Base):
    def edit(self, **w):
        driver = self.driver
        driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            driver.switch_to_frame('iframe')
            sdriver(*realname).send_keys(w['realname'])
            if w['sex'] == u'男':
                sdriver(*sexboy).click()
            elif w['sex'] == u'女':
                sdriver(*sexgirl).click()
            else:
                pass
            sdriver(*idcard).send_keys(w['idcard'])
            sdriver(*telephone).send_keys(w['telephone'])
            sdriver(*birthday).send_keys(w['birthday'])
            Select(sdriver(*province)).select_by_visible_text(w['province'])
            Select(sdriver(*city)).select_by_visible_text(w['city'])
            Select(sdriver(*country)).select_by_visible_text(w['country'])
            sdriver(*address).send_keys(w['address'])
            sdriver(*Button).click()
            driver.switch_to_default_content()
            sdriver(*okButton).click()
        except:
            return output.error_auto(driver)

        try:
            driver.switch_to_frame('iframe')
            sdriver(*realname).text
            if w['sex'] == u'男':
                sdriver(*sexboy).click()
            elif w['sex'] == u'女':
                sdriver(*sexgirl).click()
            else:
                pass
            sdriver(*idcard).text
            sdriver(*telephone).text
            sdriver(*birthday).text
            sdriver(*province).text
            sdriver(*city).text
            sdriver(*country).text
            sdriver(*address).text

            driver.switch_to_default_content()
        except:
            pass
