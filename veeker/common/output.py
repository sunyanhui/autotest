#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import config
import time
import traceback

class Model(dict):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def error_auto(driver):
    imgpath = config.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    result = {'result': False,
            'msg': traceback.format_exc() + '\n' + imgpath
    }

    return Model(**result)


def error_user_defined(driver, msg):
    imgpath = config.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    result = {'result': False,
            'msg': msg + '\n' + traceback.format_exc() + '\n'  + imgpath
    }
    return Model(**result)

def pass_auto(driver):
    imgpath = config.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    result = {'result': True,
            'msg': 'pass~'  + '\n' + imgpath
    }
    return Model(**result)

def pass_user_defined(driver, msg, **dic):
    imgpath = config.ERRORIMGPATH + str(int(time.time() * 100)) + '.jpg'
    driver.get_screenshot_as_file(imgpath)
    a = {'result': True,'msg': msg + '\n' + imgpath}
    if dic:
        return Model(**dict(a, **dic))
    else:
        return Model(**a)

class BreakException(Exception):
    pass