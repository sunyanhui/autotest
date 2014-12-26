#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_shop_customer_order_settlement import ElementCustomerOrderSettlement
from action.basepage import BasePage
from common import output

class ShopCustomerOrderSettlement(BasePage, ElementCustomerOrderSettlement):
    u'''
    联盟店客户订单结算
    '''

    def if_order_exist(self, orderNumber):
        '''
        判断订单是否存在
        :return:True / False
        '''
        driver = self.driver
        find_element = self.find_element

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            find_element(self.customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            find_element(self.order_number).send_keys(orderNumber)
            find_element(self.search).click()
        except:
            return output.error_auto(driver)

        if orderNumber in driver.page_source:
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')
