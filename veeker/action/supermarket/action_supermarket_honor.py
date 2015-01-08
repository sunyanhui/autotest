#!/usr/bin/python2.7
#coding=utf-8

import time
import re
import os
from element.element_supermarket_honor import ElementHonor
from action.basepage import BasePage
from common import output
from common.config import IMGPATH
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SupermarketHonor(BasePage, ElementHonor):
    u'''
    超市资质荣誉
    '''

    def add_honor(self, describe="random", honor_type=u"诚信资质",**kwargs):
        u'''
        新增资质
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改超市信息链接，然后切进FRAME
            find_element(self.honor_link).click()
            driver.switch_to_frame('iframe')
            num_before = self.get_list_num(self.num)
            if describe == 'random':
                describe = self.creat_random_string()

            find_element(self.add_honor_tab).click()
            self.select(find_element(self.honor_type),honor_type)
            ActionChains(driver).double_click(find_element(self.select_file)).perform()
            time.sleep(4)
            self.upload_photo(os.path.join(IMGPATH, 'logo.jpg'))
            find_element(self.describe).send_keys(describe)
            time.sleep(1)
            find_element(self.submit).click()
            num_after = self.get_list_num(self.num)
        except:
            return output.error_user_defined(driver, "新增超市荣誉失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "新增超市荣誉成功",describe = describe)
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "新增超市荣誉失败")


    def del_honor(self,describe,**kwargs):
        u'''
        新增品牌
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            #点击修改品牌管理链接，然后切进FRAME
            find_element(self.honor_link).click()
            driver.switch_to_frame('iframe')
            r = re.compile("(\d+)")
            try:
                text = find_element(self.num).text
                num_before =  int(r.findall(text)[0])
            except:
                return output.error_user_defined(driver, "没找到可以删除的超市荣誉")

            find_element((By.XPATH,"//td[text()='\n										%s']/../td[8]/input[2]"%describe)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            text = find_element(self.num).text
            num_after =  int(r.findall(text)[0])
        except:
            return output.error_user_defined(driver, "删除超市荣誉失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_before - num_after ):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "删除指定超市荣誉成功")
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "删除指定超市荣誉失败")


if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100030',password = '888888')

    b = SupermarketHonor()
    error = b.del_honor("dfgdfgfd")
    print error['msg']
    print error