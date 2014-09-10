#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.person.omycenter import *
from framework import setting
import time
import re


class Order():
    u'''
    @订单相关类
    @1、找商品
    @2、下订单
    '''

    def __init__(self, driver):

        self.driver = driver
        #self.driver = webdriver.Ie()

    def find_good(self, **w):

        driver = self.driver

        try:
            driver.find_element(*findgood).click()
            driver.switch_to_frame('iframe')
            if w['goodname'] != '':
                driver.find_element(*goodname).send_keys(w['goodname'])
            if w['startprice'] != '':
                driver.find_element(*startprice).send_keys(w['startprice'])
            if w['endprice'] != '':
                driver.find_element(*endprice).send_keys(w['endprice'])
            if w['goodclass'] != '':
                driver.find_element_by_link_text(w['goodclass']).click()
            driver.find_element(*searchButtonForFindgoods).click()

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': sys.exc_info()[1],
                    'errorimg': imgpath
            }





if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(goodname='1', startprice='1',endprice='100',goodclass=u'机构组织')
    d.get('http://www.company.com')
    print  slogin.Login(d).login('15000000372', '888888', '111')
    O = Order(d)
    #info.modify_password('888888', '888888', '888888')
    print O.find_good(**testcase)
    time.sleep(10)

    d.quit()






