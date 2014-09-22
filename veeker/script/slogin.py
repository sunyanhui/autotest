#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.ologin import *
from framework import setting, output, common_method
import time, sys



class Login():
    u'''
    登录类定义所有与登录相关的操作
    '''

    def __init__(self, driver):
        u'''
        @初始化Login对象需传入浏览器对象driver
        '''
        self.driver = driver

    def login_for_test(self, u, p, v, r):
        '''
        @该方法暂未完成，后期完善
        '''
        driver = self.driver

        #判断登录页面是否有弹窗，有的话点一下
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_id("popup_ok").click()
        except NoSuchElementException:
            pass

        #输入用户名、密码、验证码，然后点击登录按钮
        driver.find_element(username[0], username[1]).clear()
        driver.find_element(username[0], username[1]).send_keys(u)
        driver.find_element(password[0], password[1]).click()
        driver.find_element(password1[0], password1[1]).clear()
        driver.find_element(password1[0], password1[1]).send_keys(p)
        driver.find_element(verifycode[0], verifycode[1]).clear()
        driver.find_element(verifycode[0], verifycode[1]).send_keys(v)

        if r.upper() == 'YES':
            driver.find_element(rememberuseraccount[0],rememberuseraccount[1]).click()
        driver.find_element(submit[0], submit[1]).click()

        #判断是否登录成功，成功为True，失败为False
        try:
            time.sleep(1)
            driver.find_element(submit[0], submit[1])
            result = False
        except NoSuchElementException:
            result = True

        #取用户名输入框的提示语，没有为None
        try:
            ausernameprompt = driver.find_element(usernameprompt[0], usernameprompt[1]).text
            if len(ausernameprompt) < 2: ausernameprompt = None
        except NoSuchElementException:
            ausernameprompt = None

        #取密码输入框的提示语，没有为None
        try:
            apasswordprompt = driver.find_element(passwordprompt[0], passwordprompt[1]).text
            if len(apasswordprompt) < 2 : apasswordprompt = None
        except NoSuchElementException:
            apasswordprompt = None

        #取验证码输入框的提示语，没有为None
        try:
            averifycodeprompt = driver.find_element(verifycodeprompt[0], verifycodeprompt[1]).text
            if len(averifycodeprompt) < 2 : averifycodeprompt = None
        except NoSuchElementException:
            averifycodeprompt = None


        #把登录状态返回一个字典
        return {
            'result':result,
            'usernameprompt':ausernameprompt,
            'passwordprompt':apasswordprompt,
            'vertifycodeprompt':averifycodeprompt,
        }


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

        #判断登录页面是否有弹窗，有的话点一下
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_id("popup_ok").click()
        except NoSuchElementException:
            pass

        #输入用户名、密码、验证码，然后点击登录按钮
        try:
            driver.find_element(*username).clear()
            driver.find_element(*username).send_keys(w['username'])
            driver.find_element(*password).click()
            driver.find_element(*password1).clear()
            driver.find_element(*password1).send_keys(w['password'])
            driver.find_element(*verifycode).clear()
            driver.find_element(*verifycode).send_keys(w['verifycode'])
            if w['ifrememberusername'].upper() == 'YES':
                driver.find_element(*rememberuseraccount).click()
            driver.find_element(*submit).click()
        except:
            return output.error_auto(driver)

        #判断是否登录成功，成功返回True，失败返回False
        try:
            driver.implicitly_wait(10)
            driver.find_element(*logoutlink)
        except:
            return output.error_user_defined(driver, 'submint button still in , login fail')
        else:
            return output.pass_user_defined(driver, 'login succeed')

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

        if common_method.is_element_present(driver, *submit):
            return output.pass_user_defined(driver, 'logout succeed')
        else:
            return output.error_user_defined(driver, 'logout failed')


if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.company.com')
    login = Login(driver)
    log = login.login(username='15000000258',password='888888',verifycode='123',ifrememberusername='yes')
    print login.logout()
    time.sleep(3)
    driver.quit()
    print log

