#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
from element.element_person_regist import ElementRegist
from common import config, output, common
from basepage import BasePage
import time, sys, re


class Regist(BasePage, ElementRegist):
    u'''
    该类包含与注册相关的所有操作
    1、submit_information：注册信息填写页面
    2、regist：注册提交页面
    '''

    def submit_information(self, province=u'河南省',city=u'郑州市',
                           nickname='random',password='888888',confirmpassword='888888',**kwargs):
        u'''
        @该方法作用于注册信息提交页面

        @所传字典参数必须包含如下KEY
        KEY:area        省份（键值为汉字，不能输入错误）
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
            driver.find_element(*self.registerlink).click()
            driver.implicitly_wait(3)
            Select(driver.find_element(*self.province)).select_by_visible_text(province)
            Select(driver.find_element(*self.city)).select_by_visible_text(city)
            driver.find_element(*self.nickname).clear()
            if nickname=='random':
                n = str(int(time.time()*100))   #如果昵称为random，则把昵称重置为由时间生成的
                driver.find_element(*self.nickname).send_keys(n)
            else:
                driver.find_element(*self.nickname).send_keys(nickname)

            driver.find_element(*self.password).clear()
            driver.find_element(*self.password).send_keys(password)
            driver.find_element(*self.confirmpassword).clear()
            driver.find_element(*self.confirmpassword).send_keys(confirmpassword)
            driver.find_element(*self.checkbox).click()
            driver.find_element(*self.registerbutton).click()
            driver.implicitly_wait(3)
            #判断有没有email输入框
            driver.find_element(*self.email)

        except:
            return output.error_auto(driver)

        else:
            return output.pass_user_defined(driver, '信息提交成功')


    def regist(self, vertifycode='autoget', email='random' ):
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
        if email == 'random':
            email = str(int(time.time()*100))

        #填写EMAIL, 然后点击获取验证码
        try:
            driver.find_element(*self.email).clear()
            driver.find_element(*self.email).send_keys(email+'@mailcatch.com')
            driver.find_element(*self.getmailcode).click()
        except:
            return output.error_auto(driver)

        #调用获取验证码的函数并赋值
        time.sleep(15)
        if vertifycode == 'autoget':
            vertifycode = common.getvertifycode(email)

        #判断验证码的值，False返回
        if vertifycode == False:
            return output.error_user_defined(driver, "验证码获取失败")

        #执行输入验证码，然后点击提交，最后判断是否存在返回登录元素，不存在则抛异常
        try:
            driver.find_element(*self.emailcode).clear()
            driver.find_element(*self.emailcode).send_keys(vertifycode)
            driver.find_element(*self.submit).click()
            driver.implicitly_wait(5)
            regist_text = driver.find_element(*self.orderNumber).text
            num = re.compile(r'\d{11}').findall(regist_text)
            driver.find_element(*self.bact_login).click()
        except:
            return output.error_auto(driver)

        if num:
            return output.pass_user_defined(driver, '注册成功', useraccount=num[0])
        else:
            return output.error_user_defined(driver, '注册失败')
