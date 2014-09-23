#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.common.exceptions import NoSuchElementException
from watsup.winGuiAuto import findControl,setEditText, findTopWindow,clickButton
import base64

class Base():

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, driver, *ele):
        try: driver.find_element(*ele)
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

    def upload_photo(self, imgpath):
        form=findTopWindow(wantedText=u'文件上传'.encode("gb2312"))
        button=findControl(form,wantedText=u'取消'.encode("gb2312"))
        editbox=findControl(form,wantedClass='TEdit')
        #setEditText(editbox,[imgpath])
        clickButton(button)

if __name__ == '__main__':
    a =1
    print Base(a).upload_photo('c:\\img.jpg')
    #generate_html('d:/Tulips.jpg')
