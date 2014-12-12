#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from element.supermarket.element_supermarket_modify_password import *
from action.basepage import BasePage
from common import output
import time

class SupermarketModifyPassword(BasePage):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_pass(self, **w):
        u'''
        修改超市密码
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(modify_passwork_link).click()
            driver.switch_to_frame('iframe')
            find_element(old_password).clear()
            find_element(old_password).send_keys(w['oldPassword'])
            find_element(new_password).clear()
            find_element(new_password).send_keys(w['newPassword'])
            find_element(repeat_password).clear()
            find_element(repeat_password).send_keys(w['newPassword'])
            find_element(submit).click()
            time.sleep(6)
        except:
            return output.error_user_defined(driver, "修改密码失败")
        else:
            return output.pass_user_defined(driver, "密码修改成功")

