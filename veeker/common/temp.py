#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver

class base():

    cc = None

    def __init__(self):
        if base.cc == None:
            base.cc = 1
        else:
            pass
        self.cc = base.cc
        print id(self.cc)

class a(base):
    pass


class b(base):
    pass

cc = webdriver.Chrome()
cc.get()
aa = cc
cc.close()
aa = None
print cc