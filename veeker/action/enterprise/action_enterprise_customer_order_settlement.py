#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import time

from element.element_supermarket_order_query import *
from action.basepage import BasePage
from common import output


class EnterpriseCustomerOrderSettlement(BasePage):
    '''

    '''

    def if_order_exist(self, orderNumber):
        '''
        判断订单是否存在
        '''
        driver = self.driver

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            driver.find_element(*customerOrderQuery).click()
            driver.switch_to_frame('iframe')
            driver.find_element(*order_number).send_keys(orderNumber)
            driver.find_element(*search).click()
        except:
            return output.error_auto(driver)

        if u"订单编号：%s"%orderNumber in driver.page_source:
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')

    def send_out_goods(self, orderNumber):
        driver = self.driver
        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            driver.find_element(*customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            driver.find_element(*order_number).send_keys(orderNumber)
            driver.find_element(*search).click()
        except:
            return output.error_auto(driver)

        if not u"订单编号：%s"%orderNumber in driver.page_source:
            return output.error_user_defined(driver, '订单不存在')

        try:
            driver.find_element(*sendOutGoods).click()
            driver.switch_to_default_content()
            driver.find_element(*confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, '发货失败')
        else:
            return output.pass_user_defined(driver, '发货成功')


    def confirm_receipt(self, orderNumber):
        driver = self.driver
        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            driver.find_element(*customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            driver.find_element(*order_number).send_keys(orderNumber)
            driver.find_element(*search).click()
        except:
            return output.error_auto(driver)

        if not u"订单编号：%s"%orderNumber in driver.page_source:
            return output.error_user_defined(driver, '订单不存在')

        try:
            driver.find_element(*confirmReceipt).click()
            driver.switch_to_default_content()
            driver.find_element(*confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, '确认收款失败')
        else:
            return output.pass_user_defined(driver, '确认收款成功')