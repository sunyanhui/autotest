#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

#会员等级链接
vip_grade = (By.LINK_TEXT, u'会员等级')

#修改按钮
modify = (By.ID, 'modify')

#零售会员
lingshou_totalcash = (By.XPATH,"//td[text()='零售会员']/../td[2]/input")
lingshou_discount = (By.XPATH,"//td[text()='零售会员']/../td[3]/input")
lingshou_reason = (By.XPATH,"//td[text()='零售会员']/../td[4]/input")

#优惠会员
youhui_totalcash = (By.XPATH,"//td[text()='优惠会员']/../td[2]/input")
youhui_discount = (By.XPATH,"//td[text()='优惠会员']/../td[3]/input")
youhui_reason = (By.XPATH,"//td[text()='优惠会员']/../td[4]/input")

#银牌会员
yinpai_totalcash = (By.XPATH,"//td[text()='银牌会员']/../td[2]/input")
yinpai_discount = (By.XPATH,"//td[text()='银牌会员']/../td[3]/input")
yinpai_reason = (By.XPATH,"//td[text()='银牌会员']/../td[4]/input")

#金牌会员
jinpai_totalcash = (By.XPATH,"//td[text()='金牌会员']/../td[2]/input")
jinpai_discount = (By.XPATH,"//td[text()='金牌会员']/../td[3]/input")
jinpai_reason = (By.XPATH,"//td[text()='金牌会员']/../td[4]/input")

#钻石会员
zhuanshi_totalcash = (By.XPATH,"//td[text()='钻石会员']/../td[2]/input")
zhuanshi_discount = (By.XPATH,"//td[text()='钻石会员']/../td[3]/input")
zhuanshi_reason = (By.XPATH,"//td[text()='钻石会员']/../td[4]/input")

#贵宾会员
guibin_totalcash = (By.XPATH,"//td[text()='贵宾会员']/../td[2]/input")
guibin_discount = (By.XPATH,"//td[text()='贵宾会员']/../td[3]/input")
guibin_reason = (By.XPATH,"//td[text()='贵宾会员']/../td[4]/input")

#保存
submit = (By.ID, 'confirm')
