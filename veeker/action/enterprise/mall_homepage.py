#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
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
        except:
            return output.error_user_defined(driver, "获取订单数量失败~！")
        else:
            return output.pass_user_defined(driver, "获取订单数量成功~！",today_order=to)

if __name__ == '__main__':
    a = MallHomePage()
    print a.order_number("http://www.shopp100.cn")