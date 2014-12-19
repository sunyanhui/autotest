#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_enterprise_introduction import *
from action.basepage import BasePage
from common import output


class EnterpriseIntroduction(BasePage):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_introduction(self, **w):
        u'''
        修改超市介绍
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(introduction_link).click()
            driver.switch_to_frame('iframe')
            find_element(introduction).click()
            time.sleep(1)
            self.insert_html_to_richtext(introduction_rich_text, w['introduction'])
            find_element(introduction_button).click()
            driver.switch_to_default_content()
            find_element(confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改简介失败")
        else:
            return output.pass_user_defined(driver, "修改简介成功")

    def modify_culture(self, **w):
        u'''
        修改超市文件
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(introduction_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(culture).click()
            time.sleep(1)
            self.insert_html_to_richtext(culture_rich_text, w['culture'])
            find_element(culture_button).click()
            driver.switch_to_default_content()
            find_element(confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改文化失败")
        else:
            return output.pass_user_defined(driver, "修改文化成功")

    def modify_structure(self, **w):
        u'''
        修改超市组织结构
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(introduction_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(structure).click()
            time.sleep(1)
            self.insert_html_to_richtext(structure_rich_text, w['structure'])
            find_element(structure_button).click()
            driver.switch_to_default_content()
            find_element(confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改组织架构失败")
        else:
            return output.pass_user_defined(driver, "修改组织架构成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100110',password = '888888')

    b = EnterpriseIntroduction()
    error = b.modify_structure(
        structure ='''<H1>IT IS ONLY A TEST!</H1>''',
    )


    print error['msg']

    error = b.modify_introduction(**dict(
        introduction ='''<H1>IT IS ONLY A TEST!</H1>''',
    ))


    print error['msg']

    error = b.modify_culture(**dict(
        culture ='''<H1>IT IS ONLY A TEST!</H1>''',
    ))


    print error['msg']