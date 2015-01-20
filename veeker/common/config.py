#!/usr/bin/python2.7
#coding=utf-8
import os

'''
该文档用来配置一些全局变量以及一些公共配置
'''

BROWSER       = 'chrome'                           #测试用的浏览器

ERRORIMGPATH  = 'D:/errorimg/'                     #错误截图存在路径

IMGPATH       =  os.path.dirname(__file__)         #需上传图片选择路径

REPORT_RECEIVE_LIST = ['414746010@qq.com']         #报告邮件接收人

ENV = 'online'

if ENV == 'test':

    OSMS_URL      = 'http://www.wiki100.cn'        #超市版域名--测试环境

    OLMS_URL      = 'http://www.wiki168.com'       #全国版域名--测试环境

    OSMS_MALL_URL = "http://www.xiyangyang.com/"   #超市商城--测试环境

    OLSM_MALL_URL = "http://www.kamanni.com/"      #企业商城--测试环境



else:
    OSMS_URL      = 'http://www.wiki100.cn'        #超市版域名--生产环境

    OLMS_URL      = 'http://www.wiki168.com'       #全国版域名--生产环境

    OSMS_MALL_URL = "http://www.dayushangdu.com/"  #超市商城--生产环境

    OLSM_MALL_URL = "http://www.shopp100.cn/"      #企业商城--生产环境