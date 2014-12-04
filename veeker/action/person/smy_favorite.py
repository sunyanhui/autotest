#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from element.person.omy_favorite import *
from common import output, common
import time

class MyFavorite():
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()

    def but_it_now(self, **w):
        u'''
        @该方法实现点击【立即购买】进入商品详情页面功能

        @参数
        entireid：企业ID
        goodid： 商品ID

        @返回数据
        '''
        driver = self.driver
        sdriver = driver.find_element
        onclick = "buyAgainGoods('%s','%s'" %(w['goodid'],w['enterid'])

        try:
            sdriver(*myFavorites).click()
            driver.switch_to_frame('iframe')
        except InvalidSwitchToTargetException:
            return output.error_user_defined(driver, "can't enter the iframe" )
        except NoSuchElementException:
            return output.error_user_defined(driver, "can't find the myfavorites link")

        try:
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
        except:
            return output.error_user_defined(driver, "can't find the goods page")

        try:
            for i in range(int(orderpage[1])):
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick):
                    driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick)[0].click()
                    driver.switch_to_default_content()
                    driver.switch_to_window(driver.window_handles[1])
                    time.sleep(3)
                    return output.pass_user_defined(driver, 'buy it now success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except InvalidSwitchToTargetException:
            return output.error_user_defined(driver, "can't open the goodspage" )

        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, "can't find the goods")


    def undo_collection_goods(self, **w):
        u'''
        @该方法实现点击【取消收藏】功能

        @参数
        entireid：企业ID
        goodid： 商品ID

        @返回数据
        '''
        driver = self.driver
        sdriver = driver.find_element
        onclick = "buyAgainGoods('%s','%s'" %(w['goodid'],w['enterid'])

        try:
            sdriver(*myFavorites).click()
            driver.switch_to_frame('iframe')
        except InvalidSwitchToTargetException:
            return output.error_user_defined(driver, "can't enter the iframe" )
        except NoSuchElementException:
            return output.error_user_defined(driver, "can't find the myfavorites link")

        try:
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
        except:
            return output.error_user_defined(driver, "can't find the goods page")

        try:
            for i in range(int(orderpage[1])):
                #获取带有所指定LINK的对象组
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick):
                    oc = driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick)[1].get_attribute('onclick')
                    href = common.get_href_undo_myfavorite(driver.page_source, oc, u'取消收藏')
                    if not href:
                        return output.error_user_defined(driver, "can't not find the undolink")
                    sdriver(By.CSS_SELECTOR, 'a[href="%s"]'%href).click()
                    driver.switch_to_default_content()
                    sdriver(*okButton).click()
                    #此处可加总收藏数 以及 该收藏还在不在的判断，后期添加

                    return output.pass_user_defined(driver, 'undo collection success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, "can't find the goods")

    def undo_collection_shops(self, **w):
        u'''
        @该方法实现点击【取消收藏】取消商城收藏功能

        @参数
        mailurl：企业商城URL

        @返回数据
        '''
        driver = self.driver
        sdriver = driver.find_element
        onclick = "goMall('%s'" %w['mailurl']

        try:
            sdriver(*myFavorites).click()
            driver.switch_to_frame('iframe')
            sdriver(*shopscollect).click()
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                #获取带有所指定LINK的对象组
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick):
                    oc = driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick)[1].get_attribute('onclick')
                    href = common.get_href_undo_myfavorite(driver.page_source, oc, u'取消收藏')
                    if not href:
                        return output.error_user_defined(driver, "1. can't not find the undolink")
                    sdriver(By.CSS_SELECTOR, 'a[href="%s"]'%href).click()
                    driver.switch_to_default_content()
                    sdriver(*okButton).click()
                    #此处可加总收藏数 以及 该收藏还在不在的判断，后期添加

                    return output.pass_user_defined(driver, 'undo collection shop success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, "2. can't find the undolink")


    def enter_shops(self, **w):
        u'''
        @该方法实现点击【进入商城】进入商城详情页面功能

        @参数
        mailurl：企业商城URL

        @返回数据
        '''
        driver = self.driver
        sdriver = driver.find_element
        onclick = "goMall('%s'" %w['mailurl']

        try:
            sdriver(*myFavorites).click()
            driver.switch_to_frame('iframe')
            sdriver(*shopscollect).click()
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick):
                    driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="%s"]'%onclick)[0].click()
                    driver.switch_to_default_content()
                    driver.switch_to_window(driver.window_handles[1])
                    time.sleep(3)
                    return output.pass_user_defined(driver, 'enter shop success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, "can't find the shop")


if __name__ == '__main__':
    import sys, os

    #sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    #import slogin
    from action import action_login
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(username='15000001002',password='888888',ifrememberusername='YES',verifycode='1111',
                    ordernumber='101708787837000237', goodname='', startprice='', endprice='', selectindustry='',
                    mailurl='www.heping.com', goodid='224', enterid='13',
                    province=u'河南省', city=u'许昌市', country=u'鄢陵县', address='123123123123', zipcode='461200', name=u'晓晓',
                    mobile='15902165607', telephone='0371-7127556', isdefault='YES', invoice='yes',
                    payondelivery='yes', remark='1234567890', goodsnumber='5')
    d.get('http://www.enterprise.com')
    action_login.Login(d).login(**testcase)
    info = MyFavorite(d)
    ss = info.undo_collection_shops(**testcase)
    print ss['img']
    print ss['msg']
    time.sleep(3)
    #d.quit()