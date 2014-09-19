#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from framework import setting

class Browser():
    '''
    浏览器类，包含与与浏览器相关的操作
    '''

    def __init__(self):
        self.browser = setting.BROWSER #传入浏览器对象
        self.URL = setting.URL  #传入要打开的网址

    @property
    def openbrowser(self):
        browser = self.browser
        URL = str(self.URL)

        if browser.upper() == 'IE': driver = webdriver.Ie()
        elif browser.upper() == 'CHROME': driver = webdriver.Chrome()
        elif browser.upper() == 'FIREFOX': driver = webdriver.Firefox()
        elif browser.upper() == 'SAFARI': driver = webdriver.Safari()
        else: drive = webdriver.Ie()
        driver.get(URL)
        driver.maximize_window()

        return driver

if __name__ == '__main__':

    b = Browser()
    b.openbrowser
