#coding=utf-8
from selenium.webdriver.common.by import By

#************************公共对象************************#
#选择省份
province = (By.ID, 'area')

#选择市
city = (By.ID, 'city')

#选择区
country = (By.ID, 'county')

#OK按钮
okButton = (By.ID, 'popup_ok')

#保存提交按钮按钮
Button = (By.ID, 'button')

#***********************评价管理***********************#
#商品评价
goodAppraise = (By.LINK_TEXT, u'商品评价')

#评价等级
appraiseGrade = (By.ID, 'itemName')

#评价等级
selectDegrade = (By.ID, 'itemName')
#***********************投诉建议***********************#
#我的建议
mySuggest = (By.LINK_TEXT, u'我的建议')

#我的投诉
myComplain = (By.LINK_TEXT, u'我的投诉')

#***********************我的建议***********************#


#分销商申请查询
distributorQuery = (By.LINK_TEXT, u'分销商申请查询')

#退出登录
quit = (By.LINK_TEXT, u"退出登录")

