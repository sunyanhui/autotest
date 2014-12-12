#!/usr/bin/python2.7
#coding=utf-8

from element.supermarket.element_supermarket_introduction import *
from action.basepage import BasePage
from common import output
import time

class SupermarketIntroduction(BasePage):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_introduction(self, **w):
        u'''
        修改超市密码
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(introduction_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            self.insert_html_to_rich_text(introduction_rich_text, w['introduction'])
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
        修改超市密码
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
            self.insert_html_to_rich_text(culture_rich_text, w['culture'])
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
        修改超市密码
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
            self.insert_html_to_rich_text(structure_rich_text, w['structure'])
            find_element(structure_button).click()
            driver.switch_to_default_content()
            find_element(confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改文化失败")
        else:
            return output.pass_user_defined(driver, "修改文化成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(**dict(
     username = 'XYHD3100056',
     password = '888888',
    ))

    b = SupermarketIntroduction()
    error = b.modify_structure(**dict(
        structure ='''<H1>IT IS ONLY A TEST!</H1>''',
    ))


    print error['msg']