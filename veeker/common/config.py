#!/usr/bin/python2.7
#coding=utf-8
import os

'''
该文档用来配置一些全局变量以及一些公共配置
'''
#测试用的浏览器
BROWSER       = 'chrome'

#错误截图存在路径
ERRORIMGPATH  = 'D:/errorimg/'

#需上传图片选择路径
IMGPATH       =  os.path.dirname(__file__)

#报告邮件接收人
RECEIVER      = ['414746010@qq.com']

#超市版域名--生产环境
OSMS_URL      = 'http://www.wiki100.cn'

#全国版域名--生产环境
OLMS_URL      = 'http://www.wiki168.com'

#超市商城--生产环境
OSMS_MALL_URL = "http://www.dayushangdu.com/"

#企业商城--生产环境
OLSM_MALL_URL = "http://www.shopp100.cn/"

#配置测试环境，如果测试环境则为test
ENV           = 'test'