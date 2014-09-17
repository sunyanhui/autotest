#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from objectrepository.person.omycenter import *
from objectrepository.person.oplaceorder import *
from framework import error, publicmethod
import time
import re

#DEBUG = 'YES'

class PlaceOrder():



    def __init__(self, driver):
        self.driver = driver
        #if DEBUG == 'NO':self.driver = webdriver.Ie()

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
            return error.error_auto(driver)

        #建立匹配规则
        pattern = re.compile(r'\d{1,4}')

        #goodspage为总商品数量与总页数，列表结构，0：总数量，1：总页数
        goodspage = []

        try:
            goodspage = publicmethod.get_orderpage(sdriver(*totalpagenumber).text)
        except NoSuchElementException:
            goodspage = [0, 0]
        except:
            return error.error_auto(driver)

        return {'result': True, 'goodspage':goodspage, 'describtion': 'find goods Success'}

    def open_goodsdetail(self, **w):
        driver = self.driver
        sdriver = driver.find_element
        onclick = "findGoods('" + w['mailurl'] + "','" + w['goodid'] +"','" + w['enterid'] + "'"

        #判断MAILURL是不是在HOST里，如不在则添加进去
        publicmethod.modify_host(w['mailurl'])

        try:
            orderpage = publicmethod.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="'+onclick+'"]'):
                    driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="'+onclick+'"]')[0].click()
                    driver.switch_to_default_content()
                    driver.switch_to_window(driver.window_handles[1])
                    time.sleep(3)
                    return {'result': True, 'describtion': 'open goodsdetail Success'}
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return error.error_auto(driver)

        return error.error_user_defined(driver, 'not find the goods')

    def collect_goods(self):
        driver = self.driver
        sdriver = driver.find_element

        try:
            sdriver(*collect).click()
            time.sleep(3)
        except:
            return error.error_auto(driver)

        try:
            alerttext = Alert(driver).text
            Alert(driver).accept()
        except:
            return error.error_auto(driver)

        return {'result': True, 'alerttext':alerttext, 'describtion': 'collect goods Success'}

    def add_to_cart(self, **w):
        driver = self.driver
        sdriver = driver.find_element

        try:
            options = driver.find_elements(*goodsoption)
            if options:
                for i in options:
                    i.click()

            sdriver(*goodsnum).clear()
            sdriver(*goodsnum).send_keys(w['goodsnumber'])
            sdriver(*addtochat).click()
            try:Alert(driver).accept()
            except:pass
            sdriver(*gotosettle).click()
        except:
            return error.error_auto(driver)

        if publicmethod.is_element_present(driver, buynow):
            return error.error_user_defined(driver, 'add to cart failed')
        else:
            return {'result': True, 'describtion': 'add to cart Success'}


    def buy_it_now(self, **w):
        u'''
        :return:
        '''
        driver = self.driver
        sdriver = driver.find_element

        try:
            options = driver.find_elements(*goodsoption)
            if options:
                for i in options:
                    i.click()

            sdriver(*goodsnum).clear()
            sdriver(*goodsnum).send_keys(w['goodsnumber'])
            sdriver(*buynow).click()
            try:Alert(driver).accept()
            except:pass
        except:
            return error.error_auto(driver)

        if publicmethod.is_element_present(driver, *buynow):
            return error.error_user_defined(driver, 'buy it now failed')
        else:
            return {'result': True, 'describtion': 'but it now Success'}


    def order_settlement(self, **w):
        driver = self.driver
        sdriver = driver.find_element
        sdrivers = driver.find_elements
        time.sleep(3)

        if publicmethod.is_element_displayed(driver, *nulladressform):
            try:
                Select(sdrivers(*province_null)[1]).select_by_visible_text(w['province'])
                Select(sdriver(*city_null)).select_by_visible_text(w['city'])
                Select(sdriver(*country_null)).select_by_visible_text(w['country'])
                sdriver(*nulladressform).find_element(*detailaddress).clear()
                sdriver(*nulladressform).find_element(*detailaddress).send_keys(w['address'])
                sdriver(*nulladressform).find_element(*zipcode).clear()
                sdriver(*nulladressform).find_element(*zipcode).send_keys(w['zipcode'])
                sdriver(*nulladressform).find_element(*receivename).clear()
                sdriver(*nulladressform).find_element(*receivename).send_keys(w['name'])
                sdriver(*nulladressform).find_element(*mobilenumber).clear()
                sdriver(*nulladressform).find_element(*mobilenumber).send_keys(w['mobile'])
                sdriver(*nulladressform).find_element(*telephonenumber).clear()
                sdriver(*nulladressform).find_element(*telephonenumber).send_keys(w['telephone'])
                if w['isdefault'].upper() == 'YES':
                    sdriver(*nulladressform).find_element(*ifdefaultaddress).click()
                sdriver(*nulladressform).find_element(*button_null).click()
                time.sleep(3)
            except:
                return error.error_auto(driver)
        else:
            pass

        try:
            if w['invoice'].upper == 'YES':
                driver.implicitly_wait(3)
                sdriver(*invoice_yes).click()
                sdriver(*invoice_title).send_keys(w['invoicetitle'])
            elif w['invoice'].upper == 'NO':
                driver.implicitly_wait(3)
                sdriver(*invoice_no).click()
            else:
                driver.implicitly_wait(3)
                sdriver(*invoice_no).click()

            if w['payondelivery'].upper == 'YES':
                sdriver(*payondelivery).click()
            else:
                pass

            sdriver(*remark).send_keys(w['remark'])
            sdriver(*submitorder).click()

        except:
            return error.error_auto(driver)

        try:
            newordernumber = sdriver(*ordernumber).text
        except:
            error.error_user_defined(driver, 'splace order fail~!')

        return {'result':True, 'ordernumber':newordernumber,'describtion': 'splace order success'}

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import slogin
    DEBUG = 'NO'
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(ordernumber='101708787837000237',goodname='', startprice='', endprice='',selectindustry='',
                    mailurl='www.fssy.com', goodid='384',enterid='13',
                    province=u'河南省',city=u'许昌市',country=u'鄢陵县',address='123123123123',zipcode='461200',name=u'孙彦辉',
                    mobile='15902165607',telephone='0371-7127556',isdefault='YES',invoice='yes',
                    payondelivery='yes',remark='1234567890', goodsnumber='5' )
    d.get('http://www.company.com')
    slogin.Login(d).login('15000001002', '888888', '111')
    info = PlaceOrder(d)
    print info.find_goods(**testcase)
    print info.open_goodsdetail(**testcase)
    print info.add_to_cart(**testcase)
    #print info.order_settlement(**testcase)

    time.sleep(3)
    d.quit()