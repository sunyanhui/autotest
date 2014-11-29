#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-
from selenium import webdriver
from watsup.winGuiAuto import findControl,setEditText, findTopWindow,clickButton
from common import config
import os
import logging


class BasePage():

    driver = None

    def __init__(self):
        self.browser = config.BROWSER #传入浏览器对象

        if BasePage.driver == None:
            if self.browser.upper() == 'IE':BasePage.driver = webdriver.Ie()
            elif self.browser.upper() == 'CHROME': BasePage.driver = webdriver.Chrome()
            elif self.browser.upper() == 'FIREFOX': BasePage.driver = webdriver.Firefox()
            elif self.browser.upper() == 'SAFARI': BasePage.driver = webdriver.Safari()
            else: BasePage.driver = webdriver.Ie()
            BasePage.driver.maximize_window()
        else:
            pass

        self.driver = BasePage.driver

    def open_browser(self, URL):
        try:
            self.driver.get(URL)
            logging.info(u"成功打开'%s'"%URL)
            return True
        except:
            logging.error(u"打开'%s'失败"%URL)
            return False

    def quit(self):
        try:
            BasePage.driver.quit()
            BasePage.driver = None
            logging.info(u"关闭浏览器成功")
            return True
        except:
            logging.error(u"关闭浏览器失败")
            return False


    def upload_photo(self, imgpath):
        u'''
        @处理图片上传WINDOWS窗口问题

        @使用方法：传入图片路，格式为：r'Ｘ:\XX\XX.XXX'
        '''

        driver = self.driver

        if not os.path.exists(imgpath):
            return False

        if driver.name == 'chrome':
            title = u'打开'
        elif driver.name == 'Firefox':
            title = u'文件上传'
        elif driver.name == 'internet explorer':
            title = u'打开'
        else:
            title = u'打开'
        try:
            form=findTopWindow(wantedText=title.encode("gb2312"))
            button=findControl(form,wantedText=u'打开'.encode("gb2312"))
            editbox=findControl(form,wantedClass='Edit')
            setEditText(editbox,[imgpath])
            clickButton(button)
        except:
            return False
        else:
            return True

    def get_line_from_file(self, filename):
        u'''
        输入文件，从文件中读出第一行，然后删除第一行
        '''
        file_list = []
        with open(filename, 'r') as gg:
            for i in gg:
                file_list.append(i)

        with open(filename, 'w') as gg:
            for i in file_list[1:]:
                gg.write(i)

        if file_list:
            return file_list[0].strip()
        else:
            return False


if __name__ == '__main__':
    BasePage().upload_photo('d:\\Tulips.jpg')