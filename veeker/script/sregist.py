#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.oregister import *
from framework import setting
import time, urllib2, re, json, sys


class Regist():
    u'''
    定义一些与注册相关的方法
    用法：初始化时需传入浏览器句柄
    '''

    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()


    def submit_information_fortest(self, n, p, c):
        '''
        该方法后期完善，暂时先用submit_information
        后期目标：完善页面错误判断并输入至TESTCASE
        :param n:
        :param p:
        :param c:
        :return:
        '''
        driver = self.driver
        driver.find_element(registerlink[0], registerlink[1]).click()
        driver.implicitly_wait(3)
        driver.find_element(province[0], province[1]).find_element_by_xpath(province[2]).click()
        driver.find_element(city[0], city[1]).find_element_by_xpath(city[2]).click()
        driver.find_element(nickname[0], nickname[1]).clear()
        driver.find_element(nickname[0], nickname[1]).send_keys(n)
        driver.find_element(password[0], password[1]).clear()
        driver.find_element(password[0], password[1]).send_keys(p)
        driver.find_element(confirmpassword[0], confirmpassword[1]).clear()
        driver.find_element(confirmpassword[0], confirmpassword[1]).send_keys(c)
        driver.find_element(checkbox[0], checkbox[1]).click()
        driver.find_element(registerbutton[0], registerbutton[1]).click()



    def submit_information(self, n='random', p='888888', c='888888'):
        '''
        该方法用于注册填写个人信息页面，主要用来执行业务流程，不做具体的页面错误获取判断
        最终结果输入执行结果状态、错误信息以及截图即可
        :param n:昵称
        :param p:密码
        :param c:密码确认
        :return:｛执行结果，错误信息，错误截图路径｝
        '''
        driver = self.driver
        try:
            driver.find_element(registerlink[0], registerlink[1]).click()
            driver.implicitly_wait(3)
            driver.find_element(province[0], province[1]).find_element_by_xpath(province[2]).click()
            driver.find_element(city[0], city[1]).find_element_by_xpath(city[2]).click()
            driver.find_element(nickname[0], nickname[1]).clear()
            if n=='random': n = str(int(time.time()*100))   #如果昵称为random，则把昵称重置为由时间生成的
            driver.find_element(nickname[0], nickname[1]).send_keys(n)
            driver.find_element(password[0], password[1]).clear()
            driver.find_element(password[0], password[1]).send_keys(p)
            driver.find_element(confirmpassword[0], confirmpassword[1]).clear()
            driver.find_element(confirmpassword[0], confirmpassword[1]).send_keys(c)
            driver.find_element(checkbox[0], checkbox[1]).click()
            driver.find_element(registerbutton[0], registerbutton[1]).click()
            driver.implicitly_wait(3)
            driver.find_element(email[0], email[1]) #判断有没有email输入框

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':sys.exc_info()[1],
                    'errorimg':imgpath
            }

        else:
            return {'result':True,
                    'describtion':'Run ok~!',
            }


    def regist_fortest(self, emailid='random', vertifycode='autoget' ):
        '''
        @后期再优化
        :param emailid:
        :param vertifycode:
        :return:
        '''
        driver = self.driver

        if emailid == 'random':emailid = int(time.time()*100)
        driver.find_element(email[0], email[1]).clear()
        driver.find_element(email[0], email[1]).send_keys(emailid)
        driver.find_element(getmailcode[0], getmailcode[1]).click()
        if vertifycode == 'autoget': vertifycode = self.__getvertifycode(emailid)
        driver.find_element(emailcode[0], emailcode[1]).clear()
        driver.find_element(emailcode[0], emailcode[1]).send_keys(vertifycode)
        driver.find_element(submit[0], submit[1]).submit()

    def regist(self, emailid='random', vertifycode='autoget' ):
        '''
        @注册账号，提交页面脚本
        :param emailid:可选参数，如不填写，则使用随机生成的MAIL ID
        :param vertifycode:可选参数，如不填写，自动获取验证码
        :return:返回结果字典
        '''
        driver = self.driver

        #生成随机mail id
        if emailid == 'random':emailid = str(int(time.time()*100))

        #填写EMAIL, 然后点击获取验证码
        try:
            driver.find_element(email[0], email[1]).clear()
            driver.find_element(email[0], email[1]).send_keys(emailid+'@mailinator.com')
            driver.find_element(getmailcode[0], getmailcode[1]).click()
        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':sys.exc_info()[1],
                    'errorimg':imgpath
            }

        #调用获取验证码的函数并赋值
        if vertifycode == 'autoget': vertifycode = self.__getvertifycode(emailid)

        #判断验证码的值，有问题即返回
        if vertifycode == False:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':'can not get vertifycode',
                    'errorimg':imgpath
            }


        #执行输入验证码，然后点击提交，最后判断是否存在返回登录元素，不存在则抛异常
        try:
            driver.find_element(emailcode[0], emailcode[1]).clear()
            driver.find_element(emailcode[0], emailcode[1]).send_keys(vertifycode)
            driver.find_element(submit[0], submit[1]).click()
            driver.implicitly_wait(3)
            driver.find_element(backtologin[0], backtologin[1])

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':sys.exc_info()[1],
                    'errorimg':imgpath
            }

        else:
            return {'result':True,
                    'describtion':'regist succeed'
            }


    #获取验证码函数
    def __getvertifycode(self, towho):

        time.sleep(10) #等待10S，以确保能收到邮件

        #利用mailinator.com的匿名邮件功能收取验证码
        try:
            getidurl = 'https://api.mailinator.com/api/inbox?to='+towho+'&token=a65b978467f54e559c028dff740c9621'
            s = json.loads(str(urllib2.urlopen(getidurl).read()))
            mailurl = 'https://www.mailinator.com/rendermail.jsp?msgid='+s['messages'][0]['id']+'&time='+'1409663495288'
            mail = urllib2.urlopen(mailurl)
            return re.compile(r'\d{6}').search(mail.read()).group()
        except:
            return False

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.wiki168.com')
    regist = Regist(driver)
    print regist.submit_information('asdfasdfasdf7', '111111', '111111')
    print  regist.regist()
    time.sleep(5)
    driver.quit()