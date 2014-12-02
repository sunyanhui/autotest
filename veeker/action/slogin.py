#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from element.ologin import *
from action.basepage import BasePage
from common import config, output, common
import time, sys



class Login(BasePage):
    u'''
    登录类定义所有与登录相关的操作
    '''

    def login(self, **w):
        u'''
        @该方法作用于用户登录页面

        @所传字典参数必须包含如下KEY
        KEY:username           用户名
        KEY:password           密码
        KEY:verifycode         验证码
        KEY:ifrememberusername 是否记住用户名

        @返回数据
        返回如下字典格式数据
        {'result':True|False ,'msg':msg,['errorimg':imgpath]}
        '''
        driver = self.driver
        sdriver = driver.find_element


        #判断登录页面是否有弹窗，有的话点一下
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_id("popup_ok").click()
        except:
            pass

        #输入用户名、密码、验证码，然后点击登录按钮
        try:
            sdriver(*username).clear()
            sdriver(*username).send_keys(w['username'])
            sdriver(*password).click()
            sdriver(*password1).clear()
            sdriver(*password1).send_keys(w['password'])
            if w['ifrememberusername'].upper() == 'YES':
                sdriver(*rememberuseraccount).click()
            sdriver(*submit).click()
        except:
            return output.error_auto(driver)

        #判断是否登录成功，成功返回True，失败返回False
        try:
            driver.implicitly_wait(10)
            driver.find_element(*logoutlink)
        except:
            return output.error_user_defined(driver, '登录按钮还在，登录失败~!')
        else:
            return output.pass_user_defined(driver, '登录成功', title = driver.title)

    def logout(self):
        u'''
        @该方法作用于用户退出登录

        @返回数据
        返回如下字典格式数据
        {'result':True|False ,'msg':msg,['errorimg':imgpath]}
        '''

        driver = self.driver
        try:
            driver.find_element(*logoutlink).click()
            driver.implicitly_wait(3)
            driver.find_element(*logoutbutton).click()
        except:
            output.error_auto(driver)

        if common.is_element_present(driver, *submit):
            return output.pass_user_defined(driver, '登出成功')
        else:
            return output.error_user_defined(driver, '登出失败')


if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.company.com')
    login = Login()
    log = login.login(username='15000000258',password='888888',verifycode='123',ifrememberusername='yes')
    print login.logout()
    time.sleep(3)
    driver.quit()
    print log

