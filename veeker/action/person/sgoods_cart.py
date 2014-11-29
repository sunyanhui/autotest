#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from BeautifulSoup import  BeautifulSoup
from element.person.ogoods_cart import *
from common import output
from action.basepage import BasePage
import time
import re


class GoodsCart(BasePage):
    '''

    '''

    def add_to_myfavorite(self, **w):
        driver = self.driver
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

    def select_single(self, **w):
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
        else:
            return output.pass_user_defined(driver, 'select single pass~!')

    def select_more(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*goodscart).click()
            driver.switch_to_frame('iframe')
            for i in w['goodsidlist']:
                onclick = "shoppingCartAdd('%s','%s'" %(i, w['enterid'])
                checkbox_id = self.__get_href(driver.page_source, onclick, 'select_single')
                if checkbox_id == False:
                    return output.error_user_defined(driver, "can't find the checkbox")
                driver.find_element_by_id(checkbox_id).click()
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'select more pass~!')

    def select_all(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element
        onclick = "shoppingCartAdd('%s','%s'" %(w['goodsid'],w['enterid'])

        try:
            sdriver(*goodscart).click()
            driver.switch_to_frame('iframe')
            #获取第一个TR的ID,以及TR的数量，以确定最后一个TR
            trid = self.__get_href(driver.page_source, onclick, 'settlement')
            driver.find_element_by_xpath(
                "//tr[@id='%s']/td[1]/input[1]"%(trid)).click()
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'select all pass~!')

    def settlement(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element
        onclick = "shoppingCartAdd('%s','%s'" %(w['goodsid'],w['enterid'])

        try:
            #获取第一个TR的ID,以及TR的数量，以确定最后一个TR
            trid = self.__get_href(driver.page_source, onclick, 'settlement')
            driver.find_element_by_xpath(
                "//tr[@id='%s']/parent::tbody/tr[@name='accounts']/td[2]/div"%(trid)).click()
            driver.switch_to_default_content()
            prompttext = sdriver(*prompt).text
            if prompttext == u'确定结算吗？':
                sdriver(*okButton).click()
                driver.switch_to_window(driver.window_handles[1])
                return output.pass_user_defined(driver, 'goto settlement pass')
            else:
                sdriver(*okButton).click()
                return output.error_user_defined(driver, 'goto settlement failed~!')
        except:
            return output.error_user_defined(driver, 'goto settlement failed~')


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

            elif item == 'settlement':
                trid = \
                    soup.find("a", onclick=re.compile(r"%s.*"%onclick)).findParent('tbody')('tr')[0]['id']
                return trid
            else:
                return False
        except:
            return False
if __name__ == '__main__':
    from selenium import webdriver
    from action import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    testcase = dict(username='15000000237',password='888888',verifycode='1111',ifrememberusername='no',
                    goodsid='255',enterid='229',goodsidlist=['255','259','269'])
    print  slogin.Login(d).login(**testcase)
    info = GoodsCart(d)
    res =  info.select_all(**testcase)
    print res['msg']
    print info.settlement(**testcase)
    time.sleep(4)
    #d.quit()
