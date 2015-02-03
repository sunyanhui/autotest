#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

# testcase1 验证手机号输入10位数字
test_agency_basic_information_case1 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    telephone='1318303608',
    error_information=u'手机号格式不正确')

# testcase2 验证手机号输入12位数字
test_agency_basic_information_case2 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    telephone='131830360811',
    error_information=u'手机号格式不正确')


# testcase3 验证手机号输入为空
test_agency_basic_information_case3 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    telephone='',
    error_information=u'请填写信息！')


# testcase4 验证手机号输入汉字
test_agency_basic_information_case4 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    telephone=u'我是好人',
    error_information=u'手机号格式不正确')


# testcase5 验证手机号输入英文
test_agency_basic_information_case5 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    telephone='abcdefg',
    error_information=u'手机号格式不正确')

# testcase6 验证微信号输入特殊字符
test_agency_basic_information_case6 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='!@$#$',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')


# testcase7 验证微信号输入空格
test_agency_basic_information_case7 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin=' ',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')


# testcase8 验证微信号输入汉字
test_agency_basic_information_case8 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin=u'我是好人',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')

# testcase9 验证微信号输入含字母、数字、下划线和减号的字符
test_agency_basic_information_case9 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='abc_123',)

# testcase10 验证微信号输入汉字
test_agency_basic_information_case10 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='1234',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')

# testcase11 验证微信号输入大于20位的字符
test_agency_basic_information_case11 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='123456789012345678900',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')


# testcase12 验证微信号输入5~20位的字符
test_agency_basic_information_case12 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='123456',)

# testcase13 验证微信号输入为空
test_agency_basic_information_case13 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='',)

# testcase14 验证微信号输入html字符
test_agency_basic_information_case14 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    weixin='</input>',
    error_information=u'微信号格式为 5-20个字母、数字、下划线或减号！')

# testcase15 验证开户行下拉框数据
test_agency_basic_information_case15 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    bank_list=set([u"中国银行",u"中国工商银行",u"兴业银行",u"中兴银行",u"中国邮政银行",u"光大银行",u"招商银行",u"华夏银行",u"交通银行",u"浦发银行",u"请选择...",u"中国建设银行",u"郑州银行",u"中国农业银行",u"广发银行"]))

# testcase16 验证开户行所在地输入小于50个汉字
test_agency_basic_information_case16 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    location=u'一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一',)

# testcase17 验证开户行所在地输入大于50个汉字
test_agency_basic_information_case17 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    location=u'一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一',
    error_information=u'开户行所在地只能是50个汉字,150个字符')

# testcase18 验证开户行输入字母、数字、空格、汉字、特殊字符
test_agency_basic_information_case18 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    location=u'abc123  一二三㈠㈡㈢',)


# testcase19 验证开户行输入为空
test_agency_basic_information_case19 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    location='',
    error_information=u'请填写开户行所在地 ！')

# testcase20 验证对公账号输入框输入小于16个数字
test_agency_basic_information_case20 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    agency_account='111111111111111',
    error_information=u'对公账号只能是16-19位数字')

# testcase21 验证对公账号输入框输入大于19个数字
test_agency_basic_information_case21 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    agency_account='11111111111111111111',
    error_information=u'对公账号只能是16-19位数字')

# testcase22 验证对公账号输入框输入非数字的其它字符
test_agency_basic_information_case22 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    agency_account='~!@#$%^',
    error_information=u'对公账号只能是16-19位数字')

# testcase23 验证对公账号输入框输入为空
test_agency_basic_information_case23 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    agency_account='',
    error_information=u'请填写信息！')

# testcase24 验证对公账号输入框输入小于16个数字
test_agency_basic_information_case24 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    agency_account='11 111  111',
    error_information=u'对公账号只能是16-19位数字')

# testcase25 验证正确保存基本信息
test_agency_basic_information_case25 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,)