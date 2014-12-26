#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_supermarket_introduction import ElementIntroduction
from action.basepage import BasePage
from common import output


class SupermarketIntroduction(BasePage, ElementIntroduction):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_introduction(self, introduction, **kwargs):
        u'''
        修改超市介绍
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.introduction_link).click()
            driver.switch_to_frame('iframe')
            find_element(self.introduction).click()
            time.sleep(1)
            self.insert_html_to_richtext(self.introduction_rich_text[1], introduction)
            find_element(self.introduction_button).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改简介失败")
        else:
            return output.pass_user_defined(driver, "修改简介成功")

    def modify_culture(self, culture, **kwargs):
        u'''
        修改超市文件
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.introduction_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.culture).click()
            time.sleep(1)
            self.insert_html_to_richtext(self.culture_rich_text[1], culture)
            find_element(self.culture_button).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改文化失败")
        else:
            return output.pass_user_defined(driver, "修改文化成功")

    def modify_structure(self, structure, **k):
        u'''
        修改超市组织结构
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.introduction_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.structure).click()
            time.sleep(1)
            self.insert_html_to_richtext(self.structure_rich_text[1], structure)
            find_element(self.structure_button).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(3)
        except:
            return output.error_user_defined(driver, "修改组织架构失败")
        else:
            return output.pass_user_defined(driver, "修改组织架构成功")

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