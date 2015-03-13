#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from element.element_enterprise_mall_homepage import ElementMallHomepage
from action.basepage import BasePage
from common import output
import time


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


    def login(self, username, password, **kwargs):
        u'''
        @该方法作用于从商城首页登录
        '''
        driver = self.driver
        find_element = self.find_element

        #输入用户名、密码、验证码，然后点击登录按钮
        try:
            find_element(self.login_link).click()
            find_element(self.username).clear()
            find_element(self.username).send_keys(username)
            find_element(self.password1).click()
            find_element(self.password2).clear()
            find_element(self.password2).send_keys(password)
            find_element(self.submit,2).click()
            time.sleep(1)
            assert u'退出登录' in driver.page_source
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '登录成功~！')


    def search(self, goods_name, **kwargs):
        u"""
        该方法用于搜索指定商品，并打开
        """
        driver = self.driver
        find_element = self.find_element

        try:
            find_element(self.goods_name_input).clear()
            find_element(self.goods_name_input).send_keys(goods_name)
            find_element(self.search_button).click()
            driver.find_elements_by_link_text(goods_name)[1].click()
        except:
            return output.error_auto(driver)

        try:
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(2)
        except:
            return output.error_user_defined(driver, '打开商品详情页面失败')
        else:
            return output.pass_user_defined(driver, '找到指定商品，并打开详情页面')

if __name__ == '__main__':
    a = MallHomePage()
    a.open_browser("http://www.shopp100.cn/")
    print a.login('41000000024','888888')
    print a.search(u"测试专用-正常商品-企")
    time.sleep(3)
    #a.quit()
