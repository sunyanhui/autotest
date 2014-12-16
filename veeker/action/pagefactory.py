#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from action.supermarket import *
from action.agency import *
from action.enterprise import *
from action.shop import *
from action.person import *
from action import *

class PageFactory():
    u'''
    对象工厂
    '''
    @staticmethod
    def creat_po(name):
        u'''
        产生PO对象
        使用方法： 传入要生成PO的名字，规则为PO模块的名字除去ACTION_
        返回结果： 返回PO对象
        '''
        moduleName = 'action_' + name
        #根据name生成类名称，如:enterprise_role --> EnterpriseRole
        objectName = ''.join([i.capitalize() for i in name.split('_')])
        #生成PO对象
        return eval(moduleName + '.' + objectName + "()" )
