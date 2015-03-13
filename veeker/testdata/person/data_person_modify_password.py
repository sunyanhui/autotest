#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

# 测试新版个人中心修改密码
test_modify_password_case1_1 = Model(
    username=Account.person_for_modify_password,
    password=Account.person_for_modify_password_password,
    old_password = Account.person_for_modify_password_password,
    new_password = '111111',
    repeat_password = '111111')

test_modify_password_case1_2 = Model(
    username=Account.person_for_modify_password,
    password='111111',
    old_password = '111111',
    new_password = Account.person_for_modify_password_password,
    repeat_password = Account.person_for_modify_password_password)