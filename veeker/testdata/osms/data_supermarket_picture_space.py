#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from ..account import Account

#testcase1 图片空间功能
test_picture_space_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password,)
