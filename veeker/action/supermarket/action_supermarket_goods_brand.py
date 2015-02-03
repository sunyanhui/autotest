#!/usr/bin/python2.7
#coding=utf-8

import time, re
from element.element_supermarket_goods_brand import ElementGoodsBrand
from action.basepage import BasePage
from selenium.webdriver.common.by import By
from common import output

class SupermarketGoodsBrand(BasePage, ElementGoodsBrand):
    u'''
    企业品牌管理
    '''

    def add_brand(self, img_type=u"默认分类",brand_name="random",**kwargs):
        u'''
        新增品牌
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            #点击修改品牌管理链接，然后切进FRAME
            find_element(self.goods_brand_link).click()
            driver.switch_to_frame('iframe')
            r = re.compile("(\d+)")
            try:
                text = find_element(self.num, 3).text
                num_before =  int(r.findall(text)[0])
            except:
                num_before = 0

            find_element(self.add_brand_tab).click()
            select(find_element(self.select_img),img_type)
            find_element(self.photo_for_click).click()
            if brand_name == 'random':
                brand_name = self.creat_random_string()
            find_element(self.brand_name).send_keys(brand_name)
            find_element(self.submit).click()
            time.sleep(1)

            text = find_element(self.num, 3).text
            num_after =  int(r.findall(text)[0])
        except:
            return output.error_user_defined(driver, "添加商品品牌失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "添加商品品牌成功",brand_name = brand_name)
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "添加商品品牌失败")


    def del_brand(self,brand_name,**kwargs):
        u'''
        新增品牌
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            #点击修改品牌管理链接，然后切进FRAME
            find_element(self.goods_brand_link).click()
            driver.switch_to_frame('iframe')
            r = re.compile("(\d+)")
            try:
                text = find_element(self.num, 3).text
                num_before =  int(r.findall(text)[0])
            except:
                return output.error_user_defined(driver, "没找到可以删除的品牌")

            find_element((By.XPATH,"//td[text()='\n										%s']/../td[6]/input[2]"%brand_name)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            text = find_element(self.num, 3).text
            num_after =  int(r.findall(text)[0])
        except:
            return output.error_user_defined(driver, "删除商品品牌失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_before - num_after ):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "删除指定商品品牌成功")
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "删除商品品牌失败")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100030',password = '888888')

    b = SupermarketGoodsBrand()
    error = b.del_brand("mfkxgrdla")
    print error.msg