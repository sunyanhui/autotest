#coding=utf-8
from selenium.webdriver.common.by import By

#************************公共对象************************#
#选择省份
province = (By.ID, 'province')

#选择市
city = (By.ID, 'city')

#选择区
country = (By.ID, 'county')

#OK按钮
okButton = (By.ID, 'popup_ok')

#保存提交按钮按钮
Button = (By.ID, 'button')

#***********************信息中心***********************#
#密码修改链接
modifyPassword = (By.LINK_TEXT, u"密码修改")

#原密码输入框
oldPasswordInput = (By.ID, 'oldPasswordId')

#新密码输入框
newPasswordInput = (By.NAME, 'userDTO.userPassword')

#确认密码输入框
confirmPasswordInput = (By.NAME, 'repassword')

#密码修改提交按钮
passwordSubmit = (By.ID, 'button')

#修改后提示
passMessage = (By.ID, 'popup_message')

#*****************************************************#
#基本信息链接
basicinFormation = (By.LINK_TEXT, u'基本信息')

#真实姓名
realname = (By.ID, 'personName')

#姓别选项
sexboy = (By.ID, 'RadioGroup1_0')

#性别选项
sexgirl = (By.ID, 'RadioGroup1_1')

#身份证号
idcard = (By.ID, 'idCard')

#手机号
telephoneForMdInfo = (By.ID, 'telephone')

#生日选项
birthdayForMdInfo = (By.ID, 'birthday')

#详细地址
addressForMdInfo = (By.ID, 'address')

#*****************************************************#
#收货地址
shoppingAddress = (By.LINK_TEXT, u'收货地址')

#详细地址
addressForMdAd = (By.NAME, 'receiveAddDTO.addDetail')

#邮政编码
zipCodeForMdAd = (By.NAME, 'receiveAddDTO.zipCode')

#收货人
revicerNameForMdAd = (By.NAME, 'receiveAddDTO.revicerName')

#手机号码
mobileForMdAd = (By.NAME, 'receiveAddDTO.mobile')

#电话号码
telephoneForMdAd = (By.NAME, 'receiveAddDTO.telPhone')

#设为默认收货地址
isDefaultAddress = (By.NAME, 'receiveAddDTO.isDefault')

#已保存地址数
addressNumber = (By.CSS_SELECTOR, 'body p span')

#修改收货地址链接
mdaddressLink = (By.LINK_TEXT, u'修改')

#删除收货地址链接
deladdressLink = (By.LINK_TEXT, u'删除')

#***********************购物管理***********************#
#订单查询
orderQuery = (By.LINK_TEXT, u'订单查询')

#商品名称
goodsnameSearch = (By.ID, 'goodsNameSearch')

#交易状态
goodstatus = (By.ID, 'itemName', "//option[@value='vk002401']")

#搜索按钮
searchButtonFororder = (By.NAME, 'cx')

#*****************************************************#
#我的收藏
myFavorites = (By.LINK_TEXT, u'我的收藏')


#*****************************************************#
#购物车
shoppingCart = (By.LINK_TEXT, u'购物车')


#*****************************************************#
#我的抵值券
myCoupon = (By.LINK_TEXT, u'我的抵值券')

#企业名称
entername = (By.ID, 'enterName')

#有效期选择
startDateForCoupon = (By.ID, 'startDate')
endDateForCoupon = (By.ID, 'endDate')

#状态
stateForCoupon = (By.ID, 'state', "//option[@value='01']")

#搜索按钮
searchButtonForCoupon = (By.CLASS_NAME, 'btnApplyLong btnanniu')


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
#开店申请查询
shopQuery = (By.LINK_TEXT, u'开店申请查询')

#分销商申请查询
distributorQuery = (By.LINK_TEXT, u'分销商申请查询')

#退出登录
quit = (By.LINK_TEXT, u"退出登录")

