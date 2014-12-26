#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH

#testcase1 验证正常修改超市密码
test_modify_password_case1 = dict(
    username = 'XYHD3100012',
    password = '6666666',
    oldPassword = '6666666',
    newPassword = '111111',
)

#testcase2 把密码修改回来
test_modify_password_case2 = dict(
    username = 'XYHD3100012',
    password = '111111',
    oldPassword = '111111',
    newPassword = '6666666',
)