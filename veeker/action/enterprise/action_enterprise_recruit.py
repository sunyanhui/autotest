#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_enterprise_recruit import ElementRecruit
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.by import By



class EnterpriseRecruit(BasePage, ElementRecruit):
    u'''
    企业招聘信息
    '''

    def add_recruit(self, position_name='random',recruit_number='10',contact_way='0371-7981225',
                    experience='3-5年',work_property=u'全职',salary=u'面议',education=u'高中',
                    province=u'河南省',city=u'许昌市',country=u'鄢陵县',email='test@test.com',
                    describe='ITS ONLY A TEST~!',**kwargs):
        u'''
        发布招聘信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.recruit_link).click()
            driver.switch_to_frame('iframe')
            num_before = self.get_list_num(self.num)

            if position_name == "random":position_name = self.creat_random_string()
            find_element(self.add_tab).click()
            find_element(self.position_name).send_keys(position_name)
            find_element(self.recruit_number).send_keys(recruit_number)
            find_element(self.contact_way).send_keys(contact_way)
            self.select_new(self.experience, experience)
            self.select_new(self.work_property, work_property)
            self.select_new(self.salary, salary)
            self.select_new(self.education, education)
            self.select_new(self.province, province)
            self.select_new(self.city, city)
            self.select_new(self.country, country)
            find_element(self.email).send_keys(email)
            self.insert_html_to_richtext(self.describe[1], describe)
            find_element(self.submit).click()

            time.sleep(1)
            num_after = self.get_list_num(self.num)
        except:
            return output.error_user_defined(driver, "发布招聘信息失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            return output.pass_user_defined(driver, "发布招聘信息成功",position_name=position_name)
        else:
            return output.error_user_defined(driver, "发布招聘信息失败，数量没有增加")

    def del_recruit(self, title,**kwargs):
        u'''
        删除招聘信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.recruit_link).click()
            driver.switch_to_frame('iframe')

            num_before = self.get_list_num(self.num)
            find_element((By.XPATH, self.del_link[1]%title)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(1)
            driver.switch_to_frame('iframe')
            num_after = self.get_list_num(self.num)
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除公告失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_before - num_after):
            return output.pass_user_defined(driver, "删除公告成功")
        else:
            return output.error_user_defined(driver, "删除公告失败，数量没有减少")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')

    b = EnterpriseRecruit()
    error = b.add_recruit()
    b.del_recruit(error.position_name)
    #print error.msg
    print error.msg