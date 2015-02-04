#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import traceback
import time
from selenium.webdriver.common.action_chains import ActionChains
from element.element_agency_add_order import ElementAddOrder
from action.basepage import BasePage
from common import output


class AgencyAddOrder(BasePage, ElementAddOrder):
    u"""
    分销商采购订单
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
            #点击下采购单链接
            self.find_element(self.add_order_link).click()

            #切入IFRAME/*-+

            self.driver.switch_to.frame("iframe")

            #点击合作超市下拉框
            self.find_element(self.supermarket).click()

            #判断supermarket参数是否为None，如是则选择下拉框的第二个，如不是，则选择参数所设置的那个
            if supermarket is None:
                self.find_element(self.supermarket_index).click()
            else:
                self.driver.find_element_by_xpath(self.supermarket_name[1] % supermarket).click()

            #设置采购时间['name', self.date_arrival[1]]为定位列表，使用name属性定位
            self.set_time(['name', self.date_arrival[1]])

            #输入电话号码
            self.find_element(self.telephone).send_keys(telephone)

            #输入备注
            self.find_element(self.mark).send_keys(mark)

            #点击添加明细按钮
            self.find_element(self.add_list_btn, 3).click()

            #切换默认环境
            self.driver.switch_to.default_content()
            time.sleep(1)

            #点击 “我的商品” 链接
            self.find_element(self.my_goods).click()

            #点击选择按钮
            self.find_element(self.add_goods_btn).click()
            time.sleep(2)

            #把鼠标移动到右上角的X处
            #ActionChains(self.driver).move_to_element(self.find_element(self.close_btn)).perform()

            #点击X，关掉弹出窗
            try:
                self.find_element(self.close_btn,2).click()
                self.find_element(self.close_btn,2).click()
            except:
                pass

            self.driver.switch_to.frame("iframe")

            #点击提交
            self.find_element(self.submit).click()
            time.sleep(0.5)

            #判断采购单是否发布成功
            assert u"采购单发布成功" in self.driver.page_source
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "采购单发布成功")
        finally:
            self.driver.switch_to.default_content()


if __name__ == '__main__':
    import sys, os

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("41000000020", "888888")
    s = AgencyAddOrder()
    s.add()