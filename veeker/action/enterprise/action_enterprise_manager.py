#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_enterprise_manager import *
from action.basepage import BasePage
from common import output


class EnterpriseManager(BasePage):
    u'''
    企业操作员管理
    '''

    def add_manager(self, **w):
        u'''
        添加操作员
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(manager_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(add_manager).click()
            find_element(manager_account).send_keys(w['manager_account'])
            find_element(submit).click()
            self.driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "添加管理员失败")
        else:
            return output.pass_user_defined(driver, "添加管理员成功")

    def del_manager(self, **w):
        u'''
        删除操作员
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(manager_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element((By.XPATH, "//td[text()='%s']/../td[5]/input[2]"%w['manager_account'])).click()
            self.driver.switch_to_default_content()
            time.sleep(1)
            find_element(confirm).click()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除管理员失败")
        else:
            return output.pass_user_defined(driver, "删除管理员成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3101059',password = '888888')

    b = EnterpriseManager()
    error = b.del_manager(manager_account ="14000000157")
    print error['msg']