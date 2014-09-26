#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from objectrepository.person.ofind_shop import *
from framework import output, common_method
from script.page import Page
import time
import re


class FindShops(Page):

    def find_shop(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        #按输入要求搜索商家
        try:
            sdriver(*findshop).click()
            driver.switch_to_frame('iframe')
            Select(sdriver(*province)).select_by_visible_text(w['province'])
            Select(sdriver(*city)).select_by_visible_text(w['city'])
            Select(sdriver(*country)).select_by_visible_text(w['country'])
            driver.find_element_by_link_text(w['industry'])
        except:
            return output.error_auto(driver)

        try:
            shoppages = common_method.get_orderpage(sdriver(*totalpagenumber).text)
        except NoSuchElementException:
            shoppages = [0, 0]
        except:
            return output.error_auto(driver)
        finally:
            driver.switch_to_default_content()

        return output.pass_user_defined(driver, 'find shop Success', page=shoppages)

    def open_shop_detail(self, **w):
        driver = self.driver
        sdriver = driver.find_element
        onclick = "goMall('%s'"%w['mallurl']

        try:
            driver.switch_to_frame('iframe')
        except:
            return  output.error_auto(driver)

        #判断MAILURL是不是在HOST里，如不在则添加进去
        common_method.modify_host(w['mallurl'])

        try:
            orderpage = common_method.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]'):
                    driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]')[1].click()
                    driver.switch_to_default_content()
                    driver.switch_to_window(driver.window_handles[1])
                    time.sleep(3)
                    return output.pass_user_defined(driver, 'open mall success')
                if i == (int(orderpage[1]) - 1): break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not find the shop')

if __name__ == '__main__':
    from selenium import webdriver
    from script import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    province=u'全部',city=u'全部',country=u'全部',industry=u'全部',mallurl='www.22323.com'
                    )
    print  slogin.Login(d).login(**testcase)
    info = FindShops(d)
    res =  info.find_shop(**testcase)
    b = info.open_shop_detail(**testcase)
    print b['msg']
    time.sleep(4)
    d.quit()