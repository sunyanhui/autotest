#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_supermarket_goods_in_storage import ElementGoodsInStorage
from action.basepage import BasePage
from common import output

class SupermarketGoodsInStorage(BasePage, ElementGoodsInStorage):
    u'''
    企业发布商品
    '''

    def shangjia(self, goods_name):
        u'''
        下架商品商品
        '''

        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements
        select = self.select

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.goods_in_storage).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.search).click()
            if not find_elements(self.shangjia_button,1):
                return output.error_user_defined(driver, "没有找到上架商品")
            while find_elements(self.shangjia_button,1):
                find_elements(self.shangjia_button,1)[0].click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "上架商品操作执行失败")
        else:
            return output.pass_user_defined(driver, "上架商品操作执行成功")

    def xiajia(self, goods_name):
        u'''
        下架商品商品
        '''

        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements
        select = self.select

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.goods_in_storage).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.search).click()
            if not find_elements(self.xiajia_button,1):
                return output.error_user_defined(driver, "没有找到下架商品")
            while find_elements(self.xiajia_button,1):
                find_elements(self.xiajia_button,1)[0].click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "下架商品操作执行失败")
        else:
            return output.pass_user_defined(driver, "下架商品操作执行成功")

    def delete(self, goods_name):
        u'''
        下架商品商品
        '''

        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements
        select = self.select

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.goods_in_storage).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.search).click()
            while find_elements(self.delete_link,1):
                find_elements(self.delete_link,1)[0].click()
                driver.switch_to_default_content()
                find_element(self.confirm).click()
                find_element(self.confirm).click()
                driver.switch_to_frame('iframe')
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除商品操作执行失败")
        else:
            return output.pass_user_defined(driver, "删除商品操作执行成功")


if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100030',password = '888888')

    b = SupermarketGoodsInStorage()
    error = b.delete("hpjvqztaw")
    print error.msg