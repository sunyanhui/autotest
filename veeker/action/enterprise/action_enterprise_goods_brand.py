#!/usr/bin/python2.7
#coding=utf-8

import time, re
from element.element_enterprise_goods_brand import ElementGoodsBrand
from action.basepage import BasePage
from selenium.webdriver.common.by import By
from common import output

class EnterpriseGoodsBrand(BasePage, ElementGoodsBrand):
    u'''
    企业品牌管理
    '''

    def add_brand(self, img_type=u"默认分类",brand_name="random",**kwargs):
        u'''
        新增品牌
        '''

        driver = self.driver
        find_element = self.find_element
        find_elements = self.find_elements
        select = self.select

        try:
            #点击修改品牌管理链接，然后切进FRAME
            find_element(self.goods_brand_link).click()
            driver.switch_to_frame('iframe')
            if brand_name == 'random':
                brand_name = self.creat_random_string()

            find_element(self.add_button).click()
            find_elements(self.brand_name)[-1].send_keys(brand_name)
            find_element(self.save_button).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
        except:
            return output.error_user_defined(driver, "添加品牌失败")
        else:
            return output.pass_user_defined(driver, "添加品牌成功",brand_name=brand_name)
        finally:
            driver.switch_to_default_content()

    def del_brand(self,brand_name,**kwargs):
        u'''
        删除指定品牌
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            #点击修改品牌管理链接，然后切进FRAME
            find_element(self.goods_brand_link).click()
            driver.switch_to_frame('iframe')
            driver.implicitly_wait(5)
            find_element((By.XPATH, self.del_link[1]%brand_name)).click()
            find_element(self.save_button).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
        except:
            return output.error_user_defined(driver, "删除商品品牌失败")
        else:
            return output.pass_user_defined(driver, "删除指定商品品牌成功")
        finally:
            driver.switch_to_default_content()

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')

    b = EnterpriseGoodsBrand()
    error = b.del_brand("aqozfypgd")
    print error.msg