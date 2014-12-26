#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys

from element.element_supermarket_mall_homepage import ElementMallHomepage
from action.basepage import BasePage
from common import output


class MallHomePage(BasePage, ElementMallHomepage):
    u'''
    商城首页类
    '''

    def order_number(self, URL, **kwargs):
        '''
        获取商城首页订单数量
        '''
        driver = self.driver
        find_element = self.find_element

        try:
            driver.get(URL)
            to = find_element(self.today_order).text
            mo = find_element(self.month_order).text
        except:
            return output.error_user_defined(driver, "获取订单数量失败！")
        else:
            return output.pass_user_defined(driver, "获取订单数量成功！",today_order=to, month_order=mo)

if __name__ == '__main__':
    a = MallHomePage()
    print a.order_number("http://www.dayushangdu.com")