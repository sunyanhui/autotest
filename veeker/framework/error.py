#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import setting
import sys
import time

def error_auto(driver):
    imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
    driver.get_screenshot_as_file(imgpath)
    return {'result': False,
            'describtion': sys.exc_info()[1],
            'errorimg': imgpath
    }


def error_user_defined(driver, msg):
    imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
    driver.get_screenshot_as_file(imgpath)
    return {'result': False,
            'describtion': msg,
            'errorimg': imgpath
    }