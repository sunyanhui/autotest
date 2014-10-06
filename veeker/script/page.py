#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from watsup.winGuiAuto import findControl,setEditText, findTopWindow,clickButton
import base64
import os
import traceback


class Page():

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, *ele):
        try: self.driver.find_element(*ele)
        except NoSuchElementException, e: return False
        return True

    def generate_html(self, imgpath):

        try:
            with open(imgpath, 'rb') as img:
                str = base64.b64encode(img.read())
        except:
            return False
        imghtml = '''<img width="100px" height="100px" src="data:image/jpeg;base64,%s">'''%str
        return imghtml

    def upload_photo(self, driver, imgpath):
        u'''
        @处理图片上传WINDOWS窗口问题

        @使用方法：传入图片路，格式为：r'Ｘ:\XX\XX.XXX'
        '''
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
        filelist = []
        with open(filename, 'r') as gg:
            for i in gg:
                filelist.append(i)

        with open(filename, 'w') as gg:
            for i in filelist[1:]:
                gg.write(i)

        if filelist:
            return filelist[0].strip()
        else:
            return False


if __name__ == '__main__':
    #from . import sbrowser
    a =1
    Page(a).upload_photo('d:\\Tulips.jpg')
    #generate_html('d:/Tulips.jpg')
