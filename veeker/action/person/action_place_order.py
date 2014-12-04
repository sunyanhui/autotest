#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from element.person.element_place_order import *
from common import output, common
from action.basepage import BasePage
import time

class PlaceOrder(BasePage):

    def collect_goods(self):
        driver = self.driver
        sdriver = driver.find_element

        try:
            sdriver(*collect).click()
            time.sleep(3)
        except:
            return output.error_auto(driver)

        try:
            text = Alert(driver).text
            Alert(driver).accept()
        except:
            return output.error_auto(driver)

        return output.pass_user_defined(driver, 'collect goods Success', alerttext=text)

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
            try:
                Alert(driver).accept()
            except:
                pass
            sdriver(*gotosettle).click()
        except:
            return output.error_auto(driver)

        if common.is_element_present(driver, buynow):
            return output.error_user_defined(driver, 'add to cart failed')
        else:
            return output.pass_user_defined(driver, 'add to cart Success')


    def buy_it_now_normal(self, **w):
        u'''
        购买正常商品
        '''
        driver = self.driver
        sdriver = driver.find_element

        try:
            #如下代码，以后再用
            # options = driver.find_elements(*goodsoption)
            # if options:
            #     for i in options:
            #         i.click()
            #
            # sdriver(*goodsnum).clear()
            # sdriver(*goodsnum).send_keys(w['goodsnumber'])
            sdriver(*buynow).click()
            try:
                Alert(driver).accept()
            except:
                pass
        except:
            return output.error_user_defined(driver, '购买失败')
        else:
            return output.pass_user_defined(driver, '购买成功')


    def buy_it_now_group(self, **w):
        u'''
        购买团购商品
        '''
        driver = self.driver
        sdriver = driver.find_element

        try:
            sdriver(*groupnow).click()
            time.sleep(3)
            options = driver.find_elements(*select_class)
            if options:
                for i in options:
                    i.click()
            sdriver(*confirm).click()
        except:
            return output.error_user_defined(driver, '团购失败')
        else:
            return output.pass_user_defined(driver, '团购成功')

        # if common.is_element_present(driver, *buynow):
        #     return output.error_user_defined(driver, 'buy it now failed')
        # else:
        #     return output.pass_user_defined(driver, 'but it now Success')


    def order_settlement(self, **w):
        driver = self.driver
        sdriver = driver.find_element
        sdrivers = driver.find_elements
        time.sleep(3)

        # if common.is_element_displayed(driver, *nulladressform):
        #     try:
        #         Select(sdrivers(*province_null)[1]).select_by_visible_text(w['area'])
        #         Select(sdriver(*city_null)).select_by_visible_text(w['city'])
        #         Select(sdriver(*country_null)).select_by_visible_text(w['country'])
        #         sdriver(*nulladressform).find_element(*detailaddress).clear()
        #         sdriver(*nulladressform).find_element(*detailaddress).send_keys(w['address'])
        #         sdriver(*nulladressform).find_element(*zipcode).clear()
        #         sdriver(*nulladressform).find_element(*zipcode).send_keys(w['zipcode'])
        #         sdriver(*nulladressform).find_element(*receivename).clear()
        #         sdriver(*nulladressform).find_element(*receivename).send_keys(w['name'])
        #         sdriver(*nulladressform).find_element(*mobilenumber).clear()
        #         sdriver(*nulladressform).find_element(*mobilenumber).send_keys(w['mobile'])
        #         sdriver(*nulladressform).find_element(*telephonenumber).clear()
        #         sdriver(*nulladressform).find_element(*telephonenumber).send_keys(w['telephone'])
        #         if w['isdefault'].upper() == 'YES':
        #             sdriver(*nulladressform).find_element(*ifdefaultaddress).click()
        #         sdriver(*nulladressform).find_element(*button_null).click()
        #         time.sleep(3)
        #     except:
        #         return output.error_auto(driver)
        # else:
        #     pass

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

            totalPrice = sdriver(*total_price).text
            shouldPayPrice = sdriver(*should_pay_price).text
            sdriver(*remark).send_keys(w['remark'])
            sdriver(*submitorder).click()

        except:
            return output.error_auto(driver)

        try:
            newordernumber = sdriver(*ordernumber).text
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(1)
        except:
            return output.error_auto(driver)
            return output.error_user_defined(driver, '下订单失败')

        return output.pass_user_defined(driver, '下订单成功',
                                        ordernumber = newordernumber,
                                        totalPrice = totalPrice,
                                        shouldPayPrice = shouldPayPrice)


if __name__ == '__main__':
    import sys, os

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import slogin

    DEBUG = 'NO'
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    ordernumber='101708787837000237', goodname='', startprice='', endprice='', selectindustry='',
                    mailurl='www.qinyu01.com', goodid='271', enterid='229',
                    province=u'河南省', city=u'许昌市', country=u'鄢陵县', address='123123123123', zipcode='461200', name=u'孙彦辉',
                    mobile='15902165607', telephone='0371-7127556', isdefault='YES', invoice='yes',
                    payondelivery='yes', remark='1234567890', goodsnumber='5')
    d.get('http://www.enterprise.com')
    slogin.Login(d).login(**testcase)
    info = PlaceOrder(d)
    print info.find_goods(**testcase)
    print info.open_goodsdetail(**testcase)
    #print info.add_to_cart(**testcase)
    #print info.order_settlement(**testcase)

    time.sleep(3)
    #d.quit()