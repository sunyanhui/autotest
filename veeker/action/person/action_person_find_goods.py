#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import time

from element.element_person_find_goods import ElementFindGoods
from common import output, common
from action.basepage import BasePage
from selenium.webdriver.common.by import By

class FindGoods(BasePage, ElementFindGoods):

    def find_goods(self, goodname='',startprice='',endprice='',selectindustry='',**kwargs):
        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements

        #按输入要求搜索商品
        try:
            find_element(self.findgood).click()
            driver.switch_to_frame('iframe')
            find_element(self.goodname).clear()
            if goodname != '':
                find_element(self.goodname).send_keys(goodname)
            find_element(self.startprice).clear()
            if startprice != '':
                find_element(self.startprice).send_keys(startprice)
            find_element(self.endprice).clear()
            if endprice != '':
                find_element(self.endprice).click(endprice)

            #如果要找的行业分类没找到的话，暂不做处理，后期再判断
            if selectindustry != '':
                for i in find_elements(self.selectindustry):
                    if i.text == selectindustry: i.click(); break

            find_element(self.searchButtonForFindgoods).click()
        except:
            return output.error_auto(driver)

        try:
            driver.find_element_by_partial_link_text(goodname[:4]).click()
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
        #     goodspages = common.get_orderpage(find_element(self.totalpagenumber).text)
        # except NoSuchElementException:
        #     goodspages = [0, 0]
        # except:
        #     return output.error_auto(driver)
        # finally:
        #     driver.switch_to_default_content()
        # return output.pass_user_defined(driver, 'find goods Success', page=goodspages)

    # def open_goodsdetail(self, **w):
    #     driver = self.driver
    #     find_element = self.find_element
    #     find_elements = self.find_elements
    #     onclick = "findGoods('" + self.mallurl + "','" + self.goodid + "','" + enterid + "'"
    #
    #     try:
    #         driver.switch_to_frame('iframe')
    #     except:
    #         return  output.error_auto(driver)
    #
    #     #判断MAILURL是不是在HOST里，如不在则添加进去
    #     common.modify_host(mallurl)
    #
    #     try:
    #         orderpage = common.get_orderpage(find_element(self.totalpagenumber).text)
    #         for i in range(int(orderpage[1])):
    #             if driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]'):
    #                 driver.find_elements(By.CSS_SELECTOR, 'a[onclick^="' + onclick + '"]')[0].click()
    #                 driver.switch_to_default_content()
    #                 driver.switch_to_window(driver.window_handles[1])
    #                 time.sleep(3)
    #                 return output.pass_user_defined(driver, 'open goodsdetail Success')
    #             if i == (int(orderpage[1]) - 1): break
    #             find_element(self.nextpage).click()
    #     except:
    #         return output.error_auto(driver)
    #
    #     return output.error_user_defined(driver, 'not find the goods')
