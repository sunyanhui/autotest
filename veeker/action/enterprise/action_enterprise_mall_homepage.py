#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from element.element_enterprise_mall_homepage import ElementMallHomepage
from action.basepage import BasePage
from common import output


class MallHomePage(BasePage, ElementMallHomepage):
    u'''
    商城首页类
    '''

    def order_number(self, URL):
        '''
        获取商城首页订单数量
        '''
        driver = self.driver
        find_element = self.find_element

        try:
            driver.get(URL)
            to = find_element(self.today_order).text
        except:
            return output.error_user_defined(driver, "获取订单数量失败~！")
        else:
            return output.pass_user_defined(driver, "获取订单数量成功~！",today_order=to)

    def change_city(self, province, city, country):
        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements

        try:
            find_element(self.change_city).click()
            elements = find_elements(self.area)
            Select(elements[0]).select_by_visible_text(province)
            Select(elements[1]).select_by_visible_text(city)
            Select(elements[2]).select_by_visible_text(country)
            find_element(self.change_button).click()
        except:
            return output.error_user_defined(driver, "选择城市失败")

if __name__ == '__main__':
    a = MallHomePage()
    print a.order_number("http://www.shopp100.cn")