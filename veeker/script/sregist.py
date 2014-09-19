#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
from objectrepository.oregister import *
from framework import setting, output, common_method
import time, sys, re


class Regist():
    u'''
    该类包含与注册相关的所有操作
    1、submit_information：注册信息填写页面
    2、regist：注册提交页面
    '''

    def __init__(self, driver):
        u'''
        @初始化Regist对象需传入浏览器对象driver
        '''
        self.driver = driver

    def submit_information_fortest(self, **w):
        u'''
        @该方法后期完善，暂时先用submit_information
        @后期目标：完善页面错误判断并输入至TESTCASE
        '''
        pass



    def submit_information(self, **w):
        u'''
        @该方法作用于注册信息提交页面

        @所传字典参数必须包含如下KEY
        KEY:province        省份（键值为汉字，不能输入错误）
        KEY:city            地级市（键值为汉字，不能输入错误）
        KEY:nickname        昵称
        KEY:password        密码
        KEY:confirmpassword 密码确认

        @返回数据
        返回如下字典格式数据
        {'result':True|False ,'msg':msg,['errorimg':imgpath]}
        '''
        driver = self.driver
        try:
            driver.find_element(*registerlink).click()
            driver.implicitly_wait(3)
            Select(driver.find_element(*province)).select_by_visible_text(w['province'])
            Select(driver.find_element(*city)).select_by_visible_text(w['city'])
            driver.find_element(*nickname).clear()
            if w['nickname']=='random':
                n = str(int(time.time()*100))   #如果昵称为random，则把昵称重置为由时间生成的
                driver.find_element(*nickname).send_keys(n)
            else:
                driver.find_element(*nickname).send_keys(w['nickname'])

            driver.find_element(*password).clear()
            driver.find_element(*password).send_keys(w['password'])
            driver.find_element(*confirmpassword).clear()
            driver.find_element(*confirmpassword).send_keys(w['confirmpassword'])
            driver.find_element(*checkbox).click()
            driver.find_element(*registerbutton).click()
            driver.implicitly_wait(3)
            #判断有没有email输入框
            driver.find_element(*email)

        except:
            return output.error_auto(driver)

        else:
            return output.pass_user_defined(driver, 'submit information success')


    def regist_fortest(self, **w):
        u'''
        @该方法后期再优化，暂时不用
        '''
        pass


    def regist(self, **w):
        u'''
        @该方法作用于注册最终提交页面

        @所传字典参数必须包含如下KEY
        KEY:email        邮件地址，如填写random，则由程序随机生成
        KEY:vertifycode  验证码，如填写autoget，则由程序自动获取

        @返回数据
        返回如下字典格式数据
        {'result':True|False ,'msg':msg,['errorimg':imgpath]}
        '''
        driver = self.driver

        #生成随机mail id
        if w['email'] == 'random':w['email'] = str(int(time.time()*100))

        #填写EMAIL, 然后点击获取验证码
        try:
            driver.find_element(*email).clear()
            driver.find_element(*email).send_keys(w['email']+'@mailinator.com')
            driver.find_element(*getmailcode).click()
        except:
            return output.error_auto(driver)

        #调用获取验证码的函数并赋值
        if w['vertifycode'] == 'autoget': w['vertifycode'] = common_method.getvertifycode(w['email'])

        #判断验证码的值，False返回
        if w['vertifycode'] == False:
            return output.error_auto(driver)


        #执行输入验证码，然后点击提交，最后判断是否存在返回登录元素，不存在则抛异常
        try:
            driver.find_element(*emailcode).clear()
            driver.find_element(*emailcode).send_keys(w['vertifycode'])
            driver.find_element(*submit).click()
            time.sleep(5)

        except:
            return output.error_auto(driver)

        driver.implicitly_wait(5)
        registtext = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/p[1]').text
        num = re.compile(r'\d{11}').findall(registtext)

        if num:
            return output.pass_user_defined(driver, 'regist succeed', useraccount=num[0])
        else:
            return output.error_user_defined(driver, 'register fialed')

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.company.com')
    try:
        driver.implicitly_wait(2)
        driver.find_element_by_id("popup_ok").click()
    except:
        pass
    regist = Regist(driver)
    testcase = {'province':u'河南省', 'city':u'许昌市', 'nickname':'random', 'password':'111111', 'confirmpassword':'111111',
                'email':'random','vertifycode':'autoget'}

    a= regist.submit_information(**testcase)
    print a['msg']
    print  regist.regist(**testcase)
    time.sleep(5)
    driver.quit()