#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account


#testcase1 验证修改超市简介
test_modify_introduction_case1 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password,
    introduction = '''<H1>IT IS ONLY A TEST!</H1>'''
)

#testcase2 验证修改超市文化
test_modify_introduction_case2 = dict(
    username = Account.enterprise,
    password = Account.enterprise_password,
    culture = '''<H1>IT IS ONLY A TEST!</H1>'''
)

#testcase3 验证修改超市组织架构
test_modify_introduction_case3 = dict(
    username = Account.enterprise,
    password = Account.enterprise_password,
    structure = '''<H1>IT IS ONLY A TEST!</H1>'''
)