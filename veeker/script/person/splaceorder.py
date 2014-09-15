#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.person.omycenter import *
from objectrepository.person.oplaceorder import *
from framework import error, publicmethod
import time
import re

DEBUG = 'YES'

class PlaceOrder():



    def __init__(self, driver):
        self.driver = driver
        if DEBUG == 'YES':self.driver = webdriver.Ie()

    def find_goods(self, **w):
        driver = self.driver
        sdriver = driver.find_element

        #按输入要求搜索商品
        try:
            sdriver(*findgood).click()
            driver.switch_to_frame('iframe')
            sdriver(*goodname).clear()
            if w['goodname'] != '':
                sdriver(*goodname).send_keys(w['goodname'])
            sdriver(*startprice).clear()
            if w['startprice'] != '':
                sdriver(*startprice).send_keys(w['startprice'])
            sdriver(*endprice).clear()
            if w['endprice'] != '':
                sdriver(*endprice).click(w['endprice'])

            #如果要找的行业分类没找到的话，暂不做处理，后期再判断
            if w['selectindustry'] != '':
                for i in driver.find_elements(*selectindustry):
                    if i.text == w['selectindustry']: i.click(); break

            sdriver(*searchButtonForFindgoods).click()
        except:
            error.error_auto(driver)

        #建立匹配规则
        pattern = re.compile(r'\d{1,4}')

        #goodspage为总商品数量与总页数，列表结构，0：总数量，1：总页数
        try:
            goodspage = pattern.findall(sdriver(*totalpagenumber).text)
        except NoSuchElementException:
            goodspage = [0, 0]
        except:
            error.error_auto(driver)

        return {'result': True, 'goodspage':goodspage, 'describtion': 'find goods Success'}

    def open_goodsdetail(self, **w):
        driver = self.driver
        sdriver = driver.find_element

        try:
            onclick = "findGoods('" + w['mailurl'] + "','" + w['goodid'] +"','" + w['enterid'] + "'"
            driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="'+onclick+'"]')[0].click()
        except:
            error.error_auto(driver)

        driver.switch_to_default_content()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        return {'result': True, 'describtion': 'open goodsdetail Success'}

    def collect_goods(self, **w):
        pass

    def add_to_cart(self, **w):
        pass

    def buy_it_now(self, **w):
        pass

    def order_settlement(self, **w):
        pass


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import slogin
    DEBUG = 'NO'
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(ordernumber='101708787837000237',goodname='', startprice='', endprice='',selectindustry='',
                    mailurl='www.fssy.com',goodid='327',enterid='13')
    d.get('http://www.company.com')
    slogin.Login(d).login('15000000237', '888888', '111')
    info = PlaceOrder(d)
    print info.find_goods(**testcase)
    print info.open_goodsdetail(**testcase)

    time.sleep(3)

    d.quit()