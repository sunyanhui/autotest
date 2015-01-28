#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_agency_supply_order import ElementSupplyOrder
from action.basepage import BasePage
from common import output
import traceback, time, re

class AgencySupplyOrder(BasePage, ElementSupplyOrder):
    u'''
    企业供货订单
    '''

    def get_num(self,*args, **kwargs):
        u'''
        获取供货订单数量
        '''
        try:
            self.find_element(self.supply_order_link).click()
            self.driver.switch_to.frame("iframe")
            time.sleep(1)
            num = self.__get_num()
        except:
            print traceback.format_exc()
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "获取列表条数成功",num=num)
        finally:
            self.driver.switch_to.default_content()

    def repeal_order(self,*args, **kwargs):
        u'''
        撤销供货订单
        '''
        try:
            self.find_element(self.supply_order_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.order_status).click()
            self.find_element(self.unpublished).click()
            self.driver.find_elements_by_link_text(u"撤销")[0].click()
            self.driver.switch_to.default_content()
            self.find_element(self.ok_btn).click()
            self.driver.switch_to.frame('iframe')
            assert u'采购单撤销成功' in self.driver.page_source
        except:
            print traceback.format_exc()
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "撤销供货订单成功")
        finally:
            self.driver.switch_to.default_content()

    def publish(self):
        u'''
        发布供货订单
        '''
        try:
            self.find_element(self.supply_order_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.order_status).click()
            self.find_element(self.unpublished).click()
            self.driver.find_elements_by_link_text(u"发布")[0].click()
            self.driver.switch_to.default_content()
            self.find_element(self.ok_btn).click()
            self.driver.switch_to.frame('iframe')
            assert u'采购单发布成功' in self.driver.page_source
        except:
            print traceback.format_exc()
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "发布供货订单成功")
        finally:
            self.driver.switch_to.default_content()


    def __get_num(self):
        js = '''return $("div.pagelist").text()'''
        text = self.driver.execute_script(js)
        return re.search(u"共(\d*)条",text).group(1)

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("41000000020","888888")
    s = AgencySupplyOrder()
    s.repeal_order()
    time.sleep(3)
    s.quit()