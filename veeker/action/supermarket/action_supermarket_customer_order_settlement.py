#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import time

from element.element_supermarket_customer_order_settlement import ElementCustomerOrderSettlement
from action.basepage import BasePage
from common import output


class SupermarketCustomerOrderSettlement(BasePage, ElementCustomerOrderSettlement):
    u'''
    超市客户订单结算
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

        if u"订单编号：%s"%orderNumber in driver.page_source:
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')

    def send_out_goods(self, orderNumber):
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

        if not u"订单编号：%s"%orderNumber in driver.page_source:
            return output.error_user_defined(driver, '订单不存在')

        try:
            find_element(self.sendOutGoods).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, '发货失败')
        else:
            return output.pass_user_defined(driver, '发货成功')


    def confirm_receipt(self, orderNumber):
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

        if not u"订单编号：%s"%orderNumber in driver.page_source:
            return output.error_user_defined(driver, '订单不存在')

        try:
            find_element(self.confirmReceipt).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, '确认收款失败')
        else:
            return output.pass_user_defined(driver, '确认收款成功')