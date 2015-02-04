#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import traceback
import time
from selenium.webdriver.common.action_chains import ActionChains
from element.element_shop_add_order import ElementAddOrder
from action.basepage import BasePage
from common import output


class ShopAddOrder(BasePage, ElementAddOrder):
    u"""
    联盟店采购订单
    """

    def add(self, supermarket=None, telephone='13183036086', mark='only a test~!'):
        u"""
        添加采购单
        :param supermarket:
        :param telephone:
        :param mark:
        :return:
        """
        try:
            self.find_element(self.add_order_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.supermarket).click()
            if supermarket is None:
                self.find_element(self.supermarket_index).click()
            else:
                self.driver.find_element_by_xpath(self.supermarket_name[1] % supermarket).click()
            self.set_time(['name', self.date_arrival[1]])
            self.find_element(self.telephone).send_keys(telephone)
            self.find_element(self.mark).send_keys(mark)
            self.find_element(self.add_list_btn, 3).click()
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.find_element(self.my_goods).click()
            self.driver.find_element_by_xpath("(//input[@class='add_btn btn01'])[1]").click()
            time.sleep(2)
            #ActionChains(self.driver).move_to_element(self.find_element(self.close_btn)).perform()
            try:
                self.find_element(self.close_btn,2).click()
                self.find_element(self.close_btn,2).click()
            except:
                pass
            time.sleep(1)
            self.driver.switch_to.frame("iframe")
            self.find_element(self.submit).click()
            time.sleep(0.5)
            assert u"采购单添加成功" in self.driver.page_source
        except:
            print traceback.format_exc()
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "添加采购订单成功")
        finally:
            self.driver.switch_to.default_content()


if __name__ == '__main__':
    import sys, os

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("31000000001", "888888")
    s = ShopAddOrder()
    for i in range(10):
        s.add()
        # time.sleep(3)
        # s.quit()