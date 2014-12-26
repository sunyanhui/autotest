#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_enterprise_modify_password import ElementModifyPassword
from action.basepage import BasePage
from common import output


class EnterpriseModifyPassword(BasePage, ElementModifyPassword):
    u'''
    修改企业基本信息页面对象
    '''

    def modify_pass(self, **w):
        u'''
        修改超市密码
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.modify_passwork_link).click()
            driver.switch_to_frame('iframe')
            find_element(self.old_password).clear()
            find_element(self.old_password).send_keys(w['oldPassword'])
            find_element(self.new_password).clear()
            find_element(self.new_password).send_keys(w['newPassword'])
            find_element(self.repeat_password).clear()
            find_element(self.repeat_password).send_keys(w['newPassword'])
            find_element(self.submit).click()
            time.sleep(6)
        except:
            return output.error_user_defined(driver, "修改密码失败")
        else:
            return output.pass_user_defined(driver, "密码修改成功")

