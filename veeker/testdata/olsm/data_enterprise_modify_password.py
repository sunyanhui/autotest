#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH

#testcase1 验证正常修改企业密码
test_modifypass_case1 = dict(
    username = 'XYHD3100110',
    password = '888888',
    oldPassword = '888888',
    newPassword = '111111',
)

#testcase2 把密码修改回来
test_modifypass_case2 = dict(
    username = 'XYHD3100110',
    password = '111111',
    oldPassword = '111111',
    newPassword = '888888',
)