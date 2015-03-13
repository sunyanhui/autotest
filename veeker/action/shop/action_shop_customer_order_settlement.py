#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_shop_customer_order_settlement import ElementCustomerOrderSettlement
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.by import By

class ShopCustomerOrderSettlement(BasePage, ElementCustomerOrderSettlement):
    u'''
    联盟店客户订单结算
    '''

    def if_order_exist(self, order):
        u'''
        判断订单是否存在
        :return:True / False
        '''
        driver = self.driver
        find_element = self.find_element

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            find_element(self.customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            find_element(self.order_number).send_keys(order)
            find_element(self.search).click()
        except:
            return output.error_auto(driver)

        if order in driver.page_source:
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')


    def delivery(self, order,logistics_name=u'顺风',logistics_number='11111111', *args, **kwargs):
        u"""
        通过订单号码去发货
        :param orderNumber:订单号码
        :return:True / False
        """
        driver = self.driver
        find_element = self.find_element
        delivery_link = (By.XPATH,u"//span[text()='%s']/../../../tr[2]//a[text()='%s']"%(order,u"发货"))

        try:
            #点击订单查询链接-切换到iframe-输入订单编号，然后点击搜索
            find_element(self.customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            find_element(self.order_number).send_keys(order)
            find_element(self.search).click()
            find_element(delivery_link, 2).click()
            driver.switch_to_default_content()
            find_element(self.logistics_name).send_keys(logistics_name)
            find_element(self.logistics_number).send_keys(logistics_number)
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            assert u'操作成功' in driver.page_source
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '发货成功~！')
        finally:
            driver.switch_to_default_content()


    def confirm_receipt(self, order, *args, **kwargs):
        u"""
        通过订单号码去确认收款
        :param orderNumber:订单号码
        :return:True / False
        """
        driver = self.driver
        find_element = self.find_element
        confirm_receipt_link = (By.XPATH,u"//span[text()='%s']/../../../tr[2]//a[text()='%s']"%(order,u"确认收款"))

        try:
            find_element(self.customerOrderSettlement).click()
            driver.switch_to_frame('iframe')
            find_element(self.order_number).send_keys(order)
            find_element(self.search).click()
            find_element(confirm_receipt_link, 2).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            assert u'操作成功' in driver.page_source
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '确认收款成功~！')
        finally:
            driver.switch_to_default_content()

if __name__ == '__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki110.com")
    a.login('31000000001', '888888')

    b = ShopCustomerOrderSettlement()
    print b.confirm_receipt('103243134741000019')

    import time
    # time.sleep(3)
    # b.quit()
