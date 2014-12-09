#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


#首页注册链接
registerlink = (By.LINK_TEXT, u'免费注册')

#选择地区省级组定位
province = (By.ID, 'provinceAreaCode')

#选择地区市级组定位
city = (By.ID, 'juniorAreaList')

#选择地区错误提示
areaprompt = (By.ID, 'checkProvinceAreaCode')

#昵称输入框
nickname = (By.ID, 'nickName')

#密码输入框
password = (By.ID, 'userPassword')

#确认密码输入框
confirmpassword = (By.ID, 'userPasswordComfirm')

#协议确认选项框
checkbox = (By.CLASS_NAME, 'check_tb')

#注册按钮
registerbutton = (By.LINK_TEXT, u'注册')

#邮箱账号
email = (By.ID, 'email')

#验证码输入框
emailcode = (By.ID, 'emailCode')

#获取验证码
getmailcode = (By.ID, 'button')

#提交按钮
submit = (By.LINK_TEXT, u'提交')

#忘记登录密码链接
forgotPassword = (By.LINK_TEXT, u'忘记登录密码？')

#用户名输入框
userAccount = (By.ID, 'userAccount')

#验证码输入框
emailCodeForFind = (By.NAME, 'emailCode')

#下一步按钮
nextstep = (By.ID, 'submitButton')

#返回登录
bact_login = (By.LINK_TEXT, u"返回登录")

#订单号码
orderNumber = (By.XPATH, '/html/body/div[3]/div[3]/div/p[1]')