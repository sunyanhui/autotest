#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class ElementRecruit(object):

    #招聘信息链接
    recruit_link = (By.LINK_TEXT,u"超市招聘")

    #添加信息TAB页
    add_tab = (By.ID,u"two2")

    #职位名称
    position_name = (By.NAME,u"recruitDTO.position")

    #招聘人数
    recruit_number = (By.NAME,u"recruitDTO.hireNum")

    #联系方式
    contact_way = (By.NAME,u"recruitDTO.linkWay")

    #工作年限
    experience = (By.NAME,u"recruitDTO.experience")

    #工作性质
    work_property = (By.NAME,u"recruitDTO.property")

    #薪水待遇
    salary = (By.NAME,u"recruitDTO.salary")

    #学历要求
    education = (By.NAME,u"recruitDTO.education")

    #省
    province = (By.ID,u"province")

    #市
    city = (By.ID,u"city")

    #县
    country = (By.ID,u"area")

    #邮箱
    email = (By.NAME,u"recruitDTO.recruitType")

    #职位描述
    describe = (By.ID,u"content")

    #提交
    submit = (By.CLASS_NAME,u"tj_serbtn01")

    #确定按钮
    confirm = (By.ID,u"popup_ok")

    #招聘信息总数
    num = (By.CSS_SELECTOR,u"div.page_yemal p")

    #删除链接
    del_link = (By.XPATH,u"//a[text()='%s']/../../td[5]/input[2]")

