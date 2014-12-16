#!/usr/bin/python2.7
#coding=utf-8

from element.enterprise.element_enterprise_role import *
from action.basepage import BasePage
from common import output
import time

class EnterpriseRole(BasePage):
    u'''
    企业角色管理
    '''

    def add_role(self, **w):
        u'''
        添加角色
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业角色管理链接，然后切进FRAME
            find_element(role_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(add_role).click()
            find_element(role_name).send_keys(w['role_name'])
            find_element(info).click()
            find_element(submit).click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "添加角色失败")
        else:
            return output.pass_user_defined(driver, "添加角色成功")

    def del_role(self, **w):
        u'''
        删除角色
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业角色管理链接，然后切进FRAME
            find_element(role_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element((By.XPATH, "//td[text()='%s']/../td[3]/input[2]"%w['role_name'])).click()
            driver.switch_to_default_content()
            time.sleep(1)
            find_element(confirm).click()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除角色失败")
        else:
            return output.pass_user_defined(driver, "删除角色成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3101059',password = '888888')

    b = EnterpriseRole()
    error = b.add_role(role_name ="tester")
    print error['msg']