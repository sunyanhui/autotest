#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from common.config import IMGPATH

#testcase1 验证正常修改企业密码
test_modify_password_case1 = Model(
    username = 'XYHD3100018',
    password = '888888',
    oldPassword = '888888',
    newPassword = '111111',
)

#testcase2 把密码修改回来
test_modify_password_case2 = Model(
    username = 'XYHD3100018',
    password = '111111',
    oldPassword = '111111',
    newPassword = '888888',
)