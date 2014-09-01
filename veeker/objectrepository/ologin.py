#coding=utf-8
from selenium.webdriver.common.by import By

#账号输入框
username = (By.ID, 'userAccount')

#密码输入框
password = (By.ID, 'text')

#隐藏的密码输入框
password1 = (By.ID, 'userPassword')

#验证码输入框
vertifycode = (By.ID, 'txtVerifyCode')

#记住用户名
rememberuseraccount = (By.ID, 'rememberUserAccount')

#提交按钮
submit = (By.CSS_SELECTOR, 'div.btn > a')

#用户名输入错误提示
usernameprompt = (By.ID, 'userAccountSpanError')

#密码输入错误提示
passwordprompt = (By.ID, 'userPasswordSpanError')

#验证码输入错误提示
verifycodeprompt = (By.ID, 'txtVerifyCodeSpanError')