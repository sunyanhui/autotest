#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH

#testcase1 验证企业正常修改基本信息
test_modifyinfo_case1 = dict(
     username = 'XYHD3101059',
     password = '888888',
     ifrememberusername = 'yes',
     name = u'五五好好好公司',
     shot_name = u'五好公司',
     manage_type = u'专业服务',
     manage_range = u'专业服务', 
     province = u'北京',
     city = u'北京市',
     country = u'东城区',
     address = u'火星大平湖',
     mall_name = u'不对称商城',
     domain = 'www.sun.com',
     service_phone = '0371-75874512',
     complaint_phone = '0371-75874512',
     bei_an_hao = '12345678',
     wang_luo_jing_ying_xu_ke = '21345678',
     qq='123456789',
     wang_luo_an_quan_zheng_shu = '2345678',
     copyright = u'©123456',
     mall_logo = os.path.join(IMGPATH, 'logo.jpg'),
     backgroud_logo = os.path.join(IMGPATH, 'logo.jpg'),
     OR_code = os.path.join(IMGPATH, 'or.jpg'),
     ico = os.path.join(IMGPATH, 'ico.ico'),
)