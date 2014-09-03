#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.oregister import *
from framework import setting
import time, urllib2, re, json


class Regist():
    u'''
    定义一些与注册相关的方法
    用法：初始化时需传入浏览器句柄
    '''

    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()


    def submit_imformation_fortest(self, n, p, c):
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



    def submit_imformation(self, n='random', p='888888', c='888888'):
        driver = self.driver
        try:
            driver.find_element(registerlink[0], registerlink[1]).click()
            driver.implicitly_wait(3)
            driver.find_element(province[0], province[1]).find_element_by_xpath(province[2]).click()
            driver.find_element(city[0], city[1]).find_element_by_xpath(city[2]).click()
            driver.find_element(nickname[0], nickname[1]).clear()
            if n=='random': n = str(int(time.time()*100))
            driver.find_element(nickname[0], nickname[1]).send_keys(n)
            driver.find_element(password[0], password[1]).clear()
            driver.find_element(password[0], password[1]).send_keys(p)
            driver.find_element(confirmpassword[0], confirmpassword[1]).clear()
            driver.find_element(confirmpassword[0], confirmpassword[1]).send_keys(c)
            driver.find_element(checkbox[0], checkbox[1]).click()
            driver.find_element(registerbutton[0], registerbutton[1]).click()

        except NoSuchElementException, e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {
                'result':False,
                'describtion':e,
                'errorimg':imgpath
            }

        except e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }


    def regist_fortest(self, emailid='random', vertifycode='autoget' ):
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

        driver = self.driver
        if emailid == 'random':emailid = str(int(time.time()*100))

        try:
            driver.find_element(email[0], email[1]).clear()
            driver.find_element(email[0], email[1]).send_keys(emailid+'@mailinator.com')
            driver.find_element(getmailcode[0], getmailcode[1]).click()
        except NoSuchElementException, e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }
        except e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }

        if vertifycode == 'autoget': vertifycode = self.__getvertifycode(emailid)
        if vertifycode == False:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':'can not get vertifycode',
                    'errorimg':imgpath
            }
        try:
            driver.find_element(emailcode[0], emailcode[1]).clear()
            driver.find_element(emailcode[0], emailcode[1]).send_keys(vertifycode)
            driver.find_element(submit[0], submit[1]).click()
            driver.implicitly_wait(3)
            driver.find_element(backtologin[0], backtologin[1])
            return {'result':True,
                    'describtion':'regist succeed'
            }

        except NoSuchElementException, e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }

        except e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }


    def __getvertifycode(self, towho):
        time.sleep(10)
        try:
            getidurl = 'https://api.mailinator.com/api/inbox?to='+towho+'&token=a65b978467f54e559c028dff740c9621'
            s = json.loads(str(urllib2.urlopen(getidurl).read()))
            mailurl = 'https://www.mailinator.com/rendermail.jsp?msgid='+s['messages'][0]['id']+'&time='+'1409663495288'
            mail = urllib2.urlopen(mailurl)
            return re.compile(r'\d{6}').search(mail.read()).group()
        except:
            return False

if __name__ == '__main__':
    driver = webdriver.Ie()
    driver.get('http://www.wiki168.com')
    regist = Regist(driver)
    regist.submit_imformation_fortest('asdfasdfasdf4', '111111', '111111')
    log = regist.regist()
    print log
    time.sleep(5)
    driver.quit()