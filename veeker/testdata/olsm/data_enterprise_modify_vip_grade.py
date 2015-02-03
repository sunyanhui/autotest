#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from ..account import Account

#testcase1 验证正常修改会员等级
test_modify_vip_grade_case1 = Model(
    username = Account.enterprise, password = Account.enterprise_password,
    lingshou_totalcash = "1000",lingshou_discount = "90",lingshou_reason = u"测试一下",
    youhui_totalcash   = "2000",youhui_discount   = "80",youhui_reason   = u"测试一下",
    yinpai_totalcash   = "3000",yinpai_discount   = "70",yinpai_reason   = u"测试一下",
    jinpai_totalcash   = "4000",jinpai_discount   = "60",jinpai_reason   = u"测试一下",
    zhuanshi_totalcash = "5000",zhuanshi_discount = "50",zhuanshi_reason = u"测试一下",
    guibin_totalcash   = "6000",guibin_discount   = "40",guibin_reason   = u"测试一下",
)