#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_enterprise_customer_order_query import ElementCustomerOrderQuery
from action.basepage import BasePage
from common import output


class EnterpriseCustomerOrderQuery(BasePage, ElementCustomerOrderQuery):
    u'''
    企业客户订单查询
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
            find_element(self.customerOrderQuery).click()
            driver.switch_to_frame('iframe')
            find_element(self.order_number).send_keys(orderNumber)
            find_element(self.search).click()
        except:
            return output.error_auto(driver)

        if u"订单编号：%s"%orderNumber in driver.page_source:
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')