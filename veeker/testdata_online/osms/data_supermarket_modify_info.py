#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH

#testcase1 验证超市正常修改基本信息
test_modify_info_case1 = dict(
     username = 'XYHD3100012',
     password = '6666666',
     name = u'亚超超市',
     shot_name = u'亚超超市',
     manage_type = u'专业服务',
     manage_range = u'专业服务', 
     province = u'河南省',
     city = u'郑州市',
     country = u'惠济区',
     address = u'惠济区',
     mall_name = u'亚超超市',
     domain = 'www.dayushangdu.com',
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