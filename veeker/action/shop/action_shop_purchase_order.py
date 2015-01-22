#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_shop_purchase_order import ElementPurchaseOrder
from action.basepage import BasePage
from common import output

class ShopPurchaseOrder(BasePage, ElementPurchaseOrder):
    u'''
    联盟店采购订单
    '''

    def add(self, supermarket=None,):
        u'''
        添加采购单
        '''
        try:
            self.find_element(self.purchase_order_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.supermarket).click()
            time.sleep(1)
            if supermarket == None:
                self.find_element(self.supermarket_index).click()
            else:
                self.driver.find_element_by_xpath(self.supermarket_name[1]%supermarket).click()


        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "获取联盟状态成功",alliance_status_list=alliance_status_list )
        finally:
            self.driver.switch_to.default_content()



if __name__ == '__main__':
    import sys, os, time
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("31000000001","888888")
    s = ShopBusinessCooperation()
    a = s.test_alliance_status()
    print a.alliance_status_list
    b = s.search()
    print b.msg
    time.sleep(3)
    s.quit()