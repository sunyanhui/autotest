#!/usr/bin/python2.7
#coding=utf-8

import time
from selenium.webdriver.common.by import By
from element.element_supermarket_role import ElementRole
from action.basepage import BasePage
from common import output


class SupermarketRole(BasePage, ElementRole):
    u'''
    超市角色管理
    '''

    def add_role(self, role_name, **kwargs):
        u'''
        添加角色
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.role_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.add_role_tab).click()
            find_element(self.role_name).send_keys(role_name)
            find_element(self.info).click()
            find_element(self.submit).click()
            self.driver.switch_to_default_content()
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
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.role_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element((By.XPATH, "//td[text()='%s']/../td[3]/input[2]"%w['role_name'])).click()
            self.driver.switch_to_default_content()
            time.sleep(1)
            find_element(self.confirm).click()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除角色失败")
        else:
            return output.pass_user_defined(driver, "删除角色成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100056',password = '888888')

    b = SupermarketRole()
    error = b.del_role(role_name ="tester")
    print error['msg']