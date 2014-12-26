#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementModifyInfo(object):

    #修改企业信息链接
    modify_supermarket_info_link = (By.LINK_TEXT,u"修改信息")

    #企业名称输入框
    supermarket_name = (By.NAME,u"enterpriseDTO.enterName")

    #企业简称
    supermarket_short_name = (By.NAME,u"enterpriseDTO.introduction")

    #经营类型
    operate_type = (By.ID,u"industryId")

    #经营范围
    operate_range = (By.NAME,u"enterpriseDTO.businessScope")

    #区域-省
    province = (By.ID,u"province")

    #区域-市
    city = (By.ID,u"city")

    #区域-县
    country = (By.ID,u"county")

    #详细地址
    address = (By.NAME,u"enterpriseDTO.address")

    #商城LOGO
    mall_logo = (By.ID,u"mallLogo")

    #后台LOGO
    backgroud_logo = (By.ID,u"backlogo")

    #商城名称
    mall_name = (By.NAME,u"enterpriseDTO.mallName")

    #商城域名
    mall_domain = (By.NAME,u"enterpriseDTO.domain")

    #服务电话
    service_phone = (By.NAME,u"enterpriseDTO.serviceTel")

    #投诉电话
    complaint_phone = (By.NAME,u"enterpriseDTO.complaintTel")

    #备案号
    beianhao = (By.NAME,u"enterpriseDTO.icp")

    #网络经营许可证
    wangluojingyingxuke = (By.NAME,u"enterpriseDTO.netWorkLicense")

    #QQ
    qq = (By.NAME,u"enterpriseDTO.qq")

    #网络安全证书
    wangluoanquanzhengshu = (By.NAME,u"enterpriseDTO.netWorkSecurity")

    #版权信息
    copyright = (By.NAME,u"enterpriseDTO.versionInfo")

    #二维码
    OR_code = (By.ID,u"erweima")

    #企业图标
    ico = (By.ID,u"enterIco")

    #保存设置
    save = (By.CLASS_NAME,u"bcsz_btn01")

    #标题
    title = (By.CLASS_NAME,u"public_tab")

