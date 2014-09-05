#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from objectrepository.ologin import *
from framework import setting
import time, sys



class Login():
    '''
    登录类定义所有与登录相关的操作
    '''

    def __init__(self, driver):
        #self.driver = webdriver.Ie()
        self.driver = driver

    def login_for_test(self, u, p, v, r):
        '''
        @@@该方法暂未完成，后期完善，暂时TESTCASE先使用lonin()
        :param u:用户名
        :param p:密码
        :param v:验证码
        :return:返回登录状态字典
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
        driver.find_element(vertifycode[0], vertifycode[1]).clear()
        driver.find_element(vertifycode[0], vertifycode[1]).send_keys(v)

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


    def login(self, u, p, v, r='no'):
        '''
        该方法用于普通流程登录
        :param u:用户名
        :param p:密码
        :param v:验证码
        :param r:是否记住密码，默认为no，如需记住，请赋值为yes
        :return:返回状态字典
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
            driver.find_element(username[0], username[1]).clear()
            driver.find_element(username[0], username[1]).send_keys(u)
            driver.find_element(password[0], password[1]).click()
            driver.find_element(password1[0], password1[1]).clear()
            driver.find_element(password1[0], password1[1]).send_keys(p)
            driver.find_element(vertifycode[0], vertifycode[1]).clear()
            driver.find_element(vertifycode[0], vertifycode[1]).send_keys(v)
            if r.upper() == 'YES':
                driver.find_element(rememberuseraccount[0],rememberuseraccount[1]).click()
            driver.find_element(submit[0], submit[1]).click()

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':sys.exc_info()[1],
                    'errorimg':imgpath
            }

        #判断是否登录成功，成功返回True，失败返回False
        try:
            time.sleep(1)
            driver.find_element(submit[0], submit[1])

        except NoSuchElementException:
            return {'result':True,
                    'describtion':'not find submit button, login succeed'
            }

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':sys.exc_info()[1],
                    'errorimg':imgpath
            }
        else:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':'submint button still in , login fail',
                    'errorimg':imgpath
            }

if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.company.com')
    login = Login(driver)
    log = login.login('15000000258','888888','123','yes')
    time.sleep(3)
    driver.quit()
    print log

