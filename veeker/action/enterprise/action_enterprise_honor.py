#!/usr/bin/python2.7
#coding=utf-8

import time
import re
import os
from element.element_enterprise_honor import ElementHonor
from action.basepage import BasePage
from common import output
from common.config import IMGPATH
from selenium.webdriver.common.by import By


class EnterpriseHonor(BasePage, ElementHonor):
    u'''
    企业资质荣誉
    '''

    def add_honor(self, describe="random", honor_type=u"诚信资质",**kwargs):
        u'''
        新增资质
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.honor_link).click()
            driver.switch_to_frame('iframe')
            r = re.compile("(\d+)")
            try:
                text = find_element(self.num).text
                num_before =  int(r.findall(text)[0])
            except:
                num_before = 0

            if describe == 'random':
                describe = self.creat_random_string()

            find_element(self.add_honor_tab).click()
            self.select(find_element(self.honor_type),honor_type)
            find_element(self.select_file).click()
            time.sleep(1)
            self.upload_photo(os.path.join(IMGPATH, 'logo.jpg'))
            find_element(self.describe).send_keys(describe)
            time.sleep(1)
            find_element(self.submit).click()

            text = find_element(self.num).text
            num_after =  int(r.findall(text)[0])
        except:
            return output.error_user_defined(driver, "新增企业荣誉失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "新增企业荣誉成功",describe = describe)
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "新增企业荣誉失败")


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
                return output.error_user_defined(driver, "没找到可以删除的企业荣誉")

            find_element((By.XPATH,"//td[text()='\n										%s']/../td[8]/input[2]"%describe)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            text = find_element(self.num).text
            num_after =  int(r.findall(text)[0])
        except:
            return output.error_user_defined(driver, "删除企业荣誉失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_before - num_after ):
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "删除指定企业荣誉成功")
        else:
            driver.switch_to_default_content()
            return output.error_user_defined(driver, "删除指定企业荣誉失败")


if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')

    b = EnterpriseHonor()
    error = b.del_honor("1")
    print error['msg']
    print error