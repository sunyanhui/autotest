#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from objectrepository.ologin import *



class Login():
    '''
    登录类定义所有与登录相关的操作
    '''

    def __init__(self, driver):
        self.__driver = driver

    def login(self, u, p, v):
        '''
        :param userAccount:
        :param password:
        :param vertifycode:
        :return:
        '''

        self.__driver.find_element_by_id("popup_ok").click()
        self.__driver.find_element(username[0], username[1]).clear()
        self.__driver.find_element(username[0], username[1]).send_keys(u)
        self.__driver.find_element(password[0], password[1]).click()
        self.__driver.find_element(password1[0], password1[1]).clear()
        self.__driver.find_element(password1[0], password1[1]).send_keys(p)
        self.__driver.find_element(vertifycode[0], vertifycode[1]).clear()
        self.__driver.find_element(vertifycode[0], vertifycode[1]).send_keys(v)
        self.__driver.find_element(submit[0], submit[1]).click()


if __name__ == '__main__':

    driver = webdriver.Ie()

    driver.get('http://www.company.com')
    login = Login(driver)
    login.login('123','123','123')



