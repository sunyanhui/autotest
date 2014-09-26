#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from objectrepository.person.omodify_password import *
from framework import output
from script.page import Page
import time

class InfoCenter(Page):
    u'''
    个人中心 【修改密码】 下相关功能模块
    '''

    def modify_password(self, o, n ,c, **w):

        driver = self.driver

        try:
            driver.find_element(*modifyPassword).click()
            driver.switch_to_frame('iframe')
            driver.find_element(*oldPasswordInput).clear()
            driver.find_element(*oldPasswordInput).send_keys(o)
            driver.find_element(*newPasswordInput).clear()
            driver.find_element(*newPasswordInput).send_keys(n)
            driver.find_element(*confirmPasswordInput).clear()
            driver.find_element(*confirmPasswordInput).send_keys(c)
            driver.find_element(*passwordSubmit).click()

        except:
            return output.error_auto(driver)


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    print  slogin.Login(d).login('15000000372', '888888', '111')
    info = InfoCenter(d)
    print info.modify_password('888888', '888888', '888888')
    time.sleep(10)
    d.quit()
