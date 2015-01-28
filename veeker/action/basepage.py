#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from watsup.winGuiAuto import findControl,setEditText, findTopWindow,clickButton
from common import config
import os
import time
import types
import logging
import random
import traceback
import re



def exeTime(func):
    u'''
    测试函数时间装饰器
    '''
    def newFunc(*args, **args2):
        t0 = time.time()
        print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)
        back = func(*args, **args2)
        print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
        return back
    return newFunc

class BasePage(object):
    u'''
    页面基类
    '''

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
        u'''
        打开指定URL
        URL:URL地址，需加HTTP://
        True, False
        '''
        try:
            self.driver.get(URL)
            logging.info(u"成功打开'%s'"%URL)
            return True
        except:
            logging.error(u"打开'%s'失败"%URL)
            return False

    def find_element(self, element, timeout=30):
        u'''
        封装元素查找方法，简化传参方式
        element:元素定位元组，如(By.ID, 'abc')
        '''
        time.sleep(0.1)
        self.driver.implicitly_wait(timeout)
        return self.driver.find_element(*element)

    def find_elements(self, element):
        u'''
        封装元素组查找方法，简化传参方式
        element:元素定位元组，如(By.ID, 'abc')
        '''
        return self.driver.find_elements(*element)

    def select(self, element, text):
        u'''
        封装下拉框选择方法
        element:webelement对象
        text:要选择的项
        '''
        if isinstance(text, types.IntType):
            Select(element).select_by_index(text)
        else:
            Select(element).select_by_visible_text(text)

    def select_new(self, element, text):
        u'''
        封装下拉框选择方法
        element:定位元组
        text:要选择的项
        '''
        if isinstance(text, types.IntType):
            Select(self.find_element(element)).select_by_index(text)
        else:
            Select(self.find_element(element)).select_by_visible_text(text)

    def select_radio(self, radio_element, radio):
        u'''
        选择radio
        :param radio_element:radio定位元组
        :param radio: 替换字符
        '''
        self.find_element((By.XPATH, radio_element[1]%radio)).click()

    def set_time(self, name, setTime='now', timeType='day'):
        '''
        设置
        :param name    :定位属性（key, value）
        :param setTime :设置的时间，如果是now，则取当前时间
        :param timeType:设置的时间类型，有day和seconds两种选择
        '''
        if setTime == 'now' and timeType == 'seconds':
            setTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        elif setTime == 'now' and timeType == 'day':
            setTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        js = "$(\"input[%s='%s']\").attr('value','%s')"%(name[0], name[1], setTime)
        self.driver.execute_script(js)

    def quit(self):
        u'''
        退出浏览器
        '''
        try:
            BasePage.driver.quit()
            BasePage.driver = None
            logging.info(u"关闭浏览器成功")
            return True
        except:
            logging.error(u"关闭浏览器失败")
            return False

    #@exeTime
    def get_list_num(self, element):
        u'''
        获取列表条目数量
        element:列表元素定位元组
        return:列表条目数量
        '''
        r = re.compile("(\d+)")
        try:
            self.driver.implicitly_wait(2)
            text = self.find_element(element).text
            num =  int(r.findall(text)[0])
        except:
            num = 0

        return num

    def creat_random_string(self):
        u'''
        生成9位随机字母字符串
        '''
        s = ''.join(
            random.sample(
            ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],
            9)
        )
        return s

    def insert_html_to_richtext(self, id, html):
        u'''
        往富文本编辑框架里输入HTML字符
        :param id: 编辑框ID
        :param html: HTML字符
        :return:不返回，不处理异常，异常在函数外处理
        '''
        JS = "UE.getEditor('%s').execCommand('cleardoc');UE.getEditor('%s').execCommand('inserthtml','%s');"%(id,id,html)
        self.driver.execute_script(JS)

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
            #form=findTopWindow(wantedClass="#32770")
            form=findTopWindow(wantedText=title.encode("gb2312"))
            button=findControl(form,wantedText=u'打开'.encode("gb2312"))
            editbox=findControl(form,wantedClass='Edit')
            setEditText(editbox,[imgpath])
            clickButton(button)
        except:
            print traceback.format_exc()
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