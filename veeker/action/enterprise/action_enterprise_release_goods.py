#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_enterprise_release_goods import ElementReleaseGoods
from action.basepage import BasePage
from common import output



class EnterpriseReleaseGoods(BasePage, ElementReleaseGoods):
    u'''
    企业发布商品
    '''

    def release_goods(self,goods_name, goods_stock, goods_desc, price, cprice, cgprice):
        u'''
        发布商品
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.release_goods_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            select(find_element(self.goods_type),u'默认分类')
            select(find_element(self.goods_brand), 0)
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.goods_stock).send_keys(goods_stock)
            find_element(self.goods_desc).send_keys(goods_desc)
            find_element(self.price).send_keys(price)
            find_element(self.cprice).send_keys(cprice)
            find_element(self.cgprice).send_keys(cgprice)
            select(find_element(self.select_photo),u'默认分类')
            find_element(self.photo_for_click).click()
            self.insert_html_to_richtext(self.goods_desc_rich[1], goods_desc)
            find_element(self.add).click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "发布商品失败")
        else:
            return output.pass_user_defined(driver, "发布商品成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3101059',password = '888888')

    b = EnterpriseReleaseGoods()
    error = b.release_goods('111', '111', '111', '111', '111', '111')
    print error['msg']