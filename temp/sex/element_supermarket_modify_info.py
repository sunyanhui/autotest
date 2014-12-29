#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

#修改企业信息链接
modify_supermarket_info_link = (By.LINK_TEXT, u'修改信息')

#企业名称输入框
supermarket_name = (By.NAME, 'enterpriseDTO.enterName')

#企业简称
supermarket_short_name = (By.NAME, 'enterpriseDTO.introduction')

#经营类型
operate_type = (By.ID, 'industryId')

#经营范围
operate_range = (By.NAME, 'enterpriseDTO.businessScope')

#区域-省
province = (By.ID, 'province')

#区域-市
city = (By.ID, 'city')

#区域-县
country = (By.ID, 'county')

#详细地址
address = (By.NAME, 'enterpriseDTO.address')

#商城LOGO
mall_logo = (By.ID, 'mallLogo')

#后台LOGO
backgroud_logo = (By.ID, 'backlogo')

#商城名称
mall_name = (By.NAME, 'enterpriseDTO.mallName')

#商城域名
mall_domain = (By.NAME, 'enterpriseDTO.domain')

#服务电话
service_phone = (By.NAME, 'enterpriseDTO.serviceTel')

#投诉电话
complaint_phone = (By.NAME, 'enterpriseDTO.complaintTel')

#备案号
beianhao = (By.NAME, 'enterpriseDTO.icp')

#网络经营许可
wangluojingyingxuke = (By.NAME, 'enterpriseDTO.netWorkLicense')

#企业 QQ
qq = (By.NAME, 'enterpriseDTO.qq')

#网络安全证书
wangluoanquanzhengshu = (By.NAME, 'enterpriseDTO.netWorkSecurity')

#版本信息
copyright = (By.NAME, 'enterpriseDTO.versionInfo')

#二维码
OR_code = (By.ID, 'erweima')

#企业图标
ico = (By.ID, 'enterIco')

#保存设置
save = (By.CLASS_NAME, 'bcsz_btn01')

#标题
title = (By.CLASS_NAME, 'public_tab')
