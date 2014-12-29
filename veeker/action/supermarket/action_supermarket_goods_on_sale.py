#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_supermarket_goods_onsale import ElementGoodsOnsale
from action.basepage import BasePage
from common import output

class SupermarketGoodsOnsale(BasePage, ElementGoodsOnsale):
    u'''
    企业发布商品
    '''

    def xiajia(self, goods_name):
        u'''
        下架商品商品
        '''

        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.goods_onsale).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.search).click()
            if not find_elements(self.xiajia_link):
                return output.error_user_defined(driver, "没找到需要下架的商品")
            while find_elements(self.xiajia_link):
                find_elements(self.xiajia_link)[0].click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "下架商品失败")
        else:
            return output.pass_user_defined(driver, "下架商品成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100030',password = '888888')
    b = SupermarketGoodsOnsale()
    error = b.xiajia("hpjvqztaw")
    print error