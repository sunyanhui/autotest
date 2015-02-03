#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from element.element_person_login import ElementLogin
from action.basepage import BasePage
from common import config, output, common
import time, sys



class Login(BasePage, ElementLogin):
    u'''
    登录类定义所有与登录相关的操作
    '''

    def login(self, username, password ,if_remember_username='YES', **kwargs):
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

        #输入用户名、密码、验证码，然后点击登录按钮
        try:
            sdriver(*self.username).clear()
            sdriver(*self.username).send_keys(username)
            sdriver(*self.password).click()
            sdriver(*self.password1).clear()
            sdriver(*self.password1).send_keys(password)
            if if_remember_username.upper() == 'YES':
                sdriver(*self.rememberuseraccount).click()
            sdriver(*self.submit).click()
        except:
            return output.error_auto(driver)
        else:
            time.sleep(1)
            return output.pass_user_defined(driver, '登录成功~！', title = driver.title)

    def logout(self):
        u'''
        @该方法作用于用户退出登录
        '''

        driver = self.driver
        try:
            driver.find_element(*self.logoutlink).click()
            driver.implicitly_wait(3)
            driver.find_element(*self.logoutbutton).click()
        except:
            output.error_auto(driver)

        if common.is_element_present(driver, *self.submit):
            return output.pass_user_defined(driver, '登出成功')
        else:
            return output.error_user_defined(driver, '登出失败')


if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.enterprise.com')
    login = Login()
    log = login.login(username='15000000258',password='888888',verifycode='123',ifrememberusername='yes')
    print login.logout()
    time.sleep(3)
    driver.quit()
    print log

