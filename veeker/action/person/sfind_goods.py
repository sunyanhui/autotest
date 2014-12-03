#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from element.person.ofind_goods import *
from common import output, common
from action.basepage import BasePage
import time
import re


class FindGoods(BasePage):

    def find_goods(self, **w):
        driver = self.driver
        #driver = webdriver.Chrome()
        sdriver = driver.find_element

        #按输入要求搜索商品
        try:
            sdriver(*findgood).click()
            driver.switch_to_frame('iframe')
            sdriver(*goodname).clear()
            if w['goodname'] != '':
                sdriver(*goodname).send_keys(w['goodname'])
            sdriver(*startprice).clear()
            if w['startprice'] != '':
                sdriver(*startprice).send_keys(w['startprice'])
            sdriver(*endprice).clear()
            if w['endprice'] != '':
                sdriver(*endprice).click(w['endprice'])

            #如果要找的行业分类没找到的话，暂不做处理，后期再判断
            if w['selectindustry'] != '':
                for i in driver.find_elements(*selectindustry):
                    if i.text == w['selectindustry']: i.click(); break

            sdriver(*searchButtonForFindgoods).click()
        except:
            return output.error_auto(driver)

        try:
            driver.find_element_by_partial_link_text(w['goodname'][:4]).click()
            driver.switch_to_default_content()
        except:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, '没找到指定商品')

        try:
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(3)
        except:
            return output.error_user_defined(driver, '打开商品详情页面失败')
        else:
            return output.pass_user_defined(driver, '找到指定商品，并打开详情页面')

        #goodspage为总商品数量与总页数，列表结构，0：总数量，1：总页数
        # goodspages = []

        # try:
        #     goodspages = common.get_orderpage(sdriver(*totalpagenumber).text)
        # except NoSuchElementException:
        #     goodspages = [0, 0]
        # except:
        #     return output.error_auto(driver)
        # finally:
        #     driver.switch_to_default_content()
        # return output.pass_user_defined(driver, 'find goods Success', page=goodspages)

    def open_goodsdetail(self, **w):
        driver = self.driver
        sdriver = driver.find_element
        onclick = "findGoods('" + w['mallurl'] + "','" + w['goodid'] + "','" + w['enterid'] + "'"

        try:
            driver.switch_to_frame('iframe')
        except:
            return  output.error_auto(driver)

        #判断MAILURL是不是在HOST里，如不在则添加进去
        common.modify_host(w['mallurl'])

        try:
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]'):
                    driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]')[0].click()
                    driver.switch_to_default_content()
                    driver.switch_to_window(driver.window_handles[1])
                    time.sleep(3)
                    return output.pass_user_defined(driver, 'open goodsdetail Success')
                if i == (int(orderpage[1]) - 1): break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not find the goods')
