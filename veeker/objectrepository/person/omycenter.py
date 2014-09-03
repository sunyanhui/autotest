#coding=utf-8
from selenium.webdriver.common.by import By

#***********************信息中心***********************#
#密码修改链接
modifyPassword = [By.LINK_TEXT, u"密码修改"]

#原密码输入框
oldPasswordInput = [By.ID, 'oldPasswordId']

#新密码输入框
newPasswordInput = [By.NAME, 'userDTO.userPassword']

#确认密码输入框
confirmPasswordInput = [By.NAME, 'repassword']

#密码修改提交按钮
passwordSubmit = [By.ID, 'button']

#修改后提示
passMessage = [By.ID, 'popup_message']

#基本信息链接
basicinFormation = [By.LINK_TEXT, u'基本信息']

#收货地址
shoppingAddress = [By.LINK_TEXT, u'收货地址']

#***********************购物管理***********************#
#订单查询
orderQuery = [By.LINK_TEXT, u'订单查询']

#我的收藏
myFavorites = [By.LINK_TEXT, u'我的收藏']

#购物车
shoppingCart = [By.LINK_TEXT, u'购物车']

#我的抵值券
myCoupon = [By.LINK_TEXT, u'我的抵值券']

#***********************评价管理***********************#
#商品评价
goodAppraise = [By.LINK_TEXT, u'商品评价']

#***********************投诉建议***********************#
#我的建议
mySuggest = [By.LINK_TEXT, u'我的建议']

#我的投诉
myComplain = [By.LINK_TEXT, u'我的投诉']

#***********************我的建议***********************#
#开店申请查询
shopQuery = [By.LINK_TEXT, u'开店申请查询']

#分销商申请查询
distributorQuery = [By.LINK_TEXT, u'分销商申请查询']

#退出登录
quit = [By.LINK_TEXT, u"退出登录"]

#OK按钮

okButton = [By.ID, 'popup_ok']