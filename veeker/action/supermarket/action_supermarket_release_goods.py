#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_supermarket_release_goods import ElementReleaseGoods
from action.basepage import BasePage
from common import output



class SupermarketReleaseGoods(BasePage, ElementReleaseGoods):
    u'''
    企业发布商品
    '''

    def release_goods(self, goods_name="random", goods_stock="1000", goods_desc="only a test",
                      new_type_name=u'测试',new_type_value=u'测试',
                      price="999.9", cprice="999.9", cgprice="999.9", **kwargs):
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
            if goods_name == "random":
                goods_name = self.creat_random_string()
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.goods_stock).send_keys(goods_stock)
            find_element(self.goods_desc).send_keys(goods_desc)
            find_element(self.add_type).click()
            find_element(self.new_type_name).send_keys(new_type_name)
            find_element(self.new_type_value).send_keys(new_type_value)
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
            return output.pass_user_defined(driver, "发布商品成功", goods_name=goods_name)

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100030',password = '888888')

    b = SupermarketReleaseGoods()
    error = b.release_goods()
    print error