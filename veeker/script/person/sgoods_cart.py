#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from BeautifulSoup import  BeautifulSoup
from objectrepository.person.ogoods_cart import *
from framework import output, common_method
import time
import re


class GoodsCart():
    def __init__(self, driver):
        self.driver = driver


    def add_to_myfavorite(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element
        onclick = "shoppingCartAdd('%s','%s'" %(w['goodid'],w['enterid'])

        try:
            sdriver(*goodscart).click()
            driver.switch_to_frame('iframe')
            href = self.__get_href(driver.page_source, onclick, 'addtomyfavorite')
            if href == False:
                return output.error_user_defined(driver, "can't find the link")
            driver.find_element_by_css_selector("a[href='%s']"%href).click()
            driver.switch_to_default_content()
            if driver.find_elements(*prompt):
                if sdriver(*prompt).text == u'该商品已加入收藏夹，欢迎购买！！！':
                    sdriver(*okButton).click()
                    return output.pass_user_defined(driver, 'add_to myfavorite pass')
                else:
                    return output.error_user_defined(driver, 'add_to myfavorite failed')
            else:
                return output.error_user_defined(driver, 'add_to myfavorite failed')
        except:
            return output.error_auto(driver)


    def delete(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element
        onclick = "shoppingCartAdd('%s','%s'" %(w['goodid'],w['enterid'])

        try:
            sdriver(*goodscart).click()
            driver.switch_to_frame('iframe')
            href = self.__get_href(driver.page_source, onclick, 'delete')
            if href == False:
                return output.error_user_defined(driver, "can't find the link")
            driver.find_element_by_css_selector("a[href='%s']"%href).click()
            driver.switch_to_default_content()
            if driver.find_elements(*prompt):
                if sdriver(*prompt).text == u'确定要删除吗？':
                    sdriver(*okButton).click()
                    return output.pass_user_defined(driver, 'delete pass')
                else:
                    return output.error_user_defined(driver, 'delete failed')
            else:
                return output.error_user_defined(driver, 'delete failed')
        except:
            return output.error_auto(driver)

    def goto_settlement_single(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element
        onclick = "shoppingCartAdd('%s','%s'" %(w['goodid'],w['enterid'])

        try:
            sdriver(*goodscart).click()
            driver.switch_to_frame('iframe')
            checkbox_id = self.__get_href(driver.page_source, onclick, 'select_single')
            if checkbox_id == False:
                return output.error_user_defined(driver, "can't find the checkbox")
            driver.find_element_by_id(checkbox_id).click()
        except:
            return output.error_auto(driver)

    def goto_settlement_all(self):
        pass

    def goods_detail(self):
        pass

    def __get_href(self, page, onclick, item):

        try:
            soup = BeautifulSoup(''.join(page))
            onclick = onclick.replace('(', '\(')
        except:
            return False

        try:
            if item == 'addtomyfavorite':
                add_to_myfavorite_link = \
                    soup.find("a", onclick=re.compile(r"%s.*"%onclick)).findParent('tr')('td')[6]('a')[0]
                if add_to_myfavorite_link.string == u'移入收藏':return add_to_myfavorite_link['href']
                else:return False

            elif item == 'delete':
                delete_link = \
                    soup.find("a", onclick=re.compile(r"%s.*"%onclick)).findParent('tr')('td')[6]('a')[1]
                if delete_link.string == u'删除':return delete_link['href']
                else:return False

            elif item == 'select_single':
                select_single_link = \
                    soup.find("a", onclick=re.compile(r"%s.*"%onclick)).findParent('tr')('td')[0]('input')[0]
                if select_single_link['type'] == 'checkbox':return select_single_link['id']
                else:return False

            else:
                return False
        except:
            return False
if __name__ == '__main__':
    from selenium import webdriver
    from script import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    testcase = dict(username='15000000237',password='888888',verifycode='1111',ifrememberusername='no',
                    goodid='362',enterid='11',)
    print  slogin.Login(d).login(**testcase)
    info = GoodsCart(d)
    res =  info.goto_settlement_single(**testcase)
    print res['msg']
    #time.sleep(4)
    #d.quit()
