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
