#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from objectrepository.ologin import *
import time



class Login():
    '''
    登录类定义所有与登录相关的操作
    '''

    def __init__(self, driver):
        #self.driver = webdriver.Ie()
        self.driver = driver

    def login(self, u, p, v):
        '''

        :param u:
        :param p:
        :param v:
        :return:
        '''
        driver = self.driver

        try:
            driver.implicitly_wait(3)
            driver.find_element_by_id("popup_ok").click()
        except NoSuchElementException:
            pass

        driver.find_element(username[0], username[1]).clear()
        driver.find_element(username[0], username[1]).send_keys(u)
        driver.find_element(password[0], password[1]).click()
        driver.find_element(password1[0], password1[1]).clear()
        driver.find_element(password1[0], password1[1]).send_keys(p)
        driver.find_element(vertifycode[0], vertifycode[1]).clear()
        driver.find_element(vertifycode[0], vertifycode[1]).send_keys(v)
        driver.find_element(submit[0], submit[1]).click()

        try:
            time.sleep(1)
            driver.find_element(submit[0], submit[1])
            result = False
            ausernameprompt = driver.find_element(usernameprompt[0], usernameprompt[1]).text
            apasswordprompt = driver.find_element(passwordprompt[0], passwordprompt[1]).text
            averifycodeprompt = driver.find_element(verifycodeprompt[0], verifycodeprompt[1]).text

        except NoSuchElementException, e:
            print e
            result = True
            ausernameprompt = None
            apasswordprompt = None
            averifycodeprompt = None

        return {
            'result':result,
            'usernameprompt':ausernameprompt,
            'passwordprompt':apasswordprompt,
            'verifycodeprompt':averifycodeprompt,
        }


if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.company.com')
    login = Login(driver)
    log = login.login('15000000248','888888','123')
    time.sleep(3)
    driver.quit()
    print log.values()

