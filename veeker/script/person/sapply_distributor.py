#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from objectrepository.person.oapply_distributor import *
from framework import output
from script.sbase import Base
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class ApplyDistributor(Base):

    def apply_distributor(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*apply_distributor).click()
            driver.switch_to_frame('iframe')
            Select(sdriver(*mode)).select_by_visible_text(w['mode'])
            Select(sdriver(*grade)).select_by_visible_text(w['grade'])
            sdriver(*company_name).clear()
            if not w['companyname'] == '':
                sdriver(*company_name).send_keys(w['companyname'])
            sdriver(*search_button).click()
        except:
            return output.error_auto(driver)




if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    mode=u'分销服务代理',grade=u'省级分销商',companyname='',
                    )
    print  slogin.Login(d).login(**testcase)
    info = ApplyDistributor(d)
    res =  info.apply_distributor(**testcase)
    print res['msg']
    time.sleep(10)