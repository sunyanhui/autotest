#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import setting
import sys
import time
import traceback


def error_auto(driver):
    imgpath = setting.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    return {'result': False,
            'msg': traceback.format_exc(),
            'img': imgpath
    }


def error_user_defined(driver, msg):
    imgpath = setting.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    return {'result': False,
            'msg': msg,
            'img': imgpath
    }

def pass_auto(driver):
    imgpath = setting.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    return {'result': True,
            'msg': 'pass~',
            'img': imgpath
    }

def pass_user_defined(driver, msg, **dic):
    imgpath = setting.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    a = {'result': True,'msg': msg,'img': imgpath}
    if dic:
        return dict(a, **dic)
    else:
        return a

class BreakException(Exception):
    pass