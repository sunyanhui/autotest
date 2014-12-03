#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from element.enterprise.mall_homepage import *
from action.basepage import BasePage
from common import output

class MallHomePage(BasePage):
    u'''
    商城首页类
    '''

    def order_number(self, URL):
        '''
        获取商城首页订单数量
        '''
        driver = self.driver
        sdriver = driver.find_element

        try:
            driver.get(URL)
            to = sdriver(*today_order).text
            mo = sdriver(*month_order).text
        except:
            return output.error_user_defined(driver, "获取订单数量失败~！")
        else:
            return output.pass_user_defined(driver, "获取订单数量成功~！",today_order=to, month_order=mo)

if __name__ == '__main__':
    a = MallHomePage()
    b = {'mall_url':"http://www.dayushangdu.com"}
    print a.order_number(**b)