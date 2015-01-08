#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_enterprise_release_zhaoshang_information import ElementReleaseZhaoshangInformation
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.by import By



class EnterpriseReleaseZhaoshangInformation(BasePage, ElementReleaseZhaoshangInformation):
    u'''
    企业招商信息
    '''

    def add(self,
                 grade   = u'省级分销商',
                 require = u'测试一下',
                 mode    = u'采购代理',
                 remark  = u'测试一下',*args, **kwargs):
        u'''
        新增招商信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select_new
        select_radio = self.select_radio

        try:
            find_element(self.release_zhaoshang_information_link).click()
            driver.switch_to_frame('iframe')
            num_before = self.get_list_num(self.num)
            find_element(self.add_tab).click()
            select(self.grade, grade)
            select_radio(self.mode, mode)
            #find_element((By.XPATH, self.mode[1]%mode)).click()
            find_element(self.require).send_keys(require)
            find_element(self.remark).send_keys(remark)
            find_element(self.submit).click()
            time.sleep(4)
            num_after = self.get_list_num(self.num)
        except:
            return output.error_user_defined(driver, "发布招商信息失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            return output.pass_user_defined(driver, "发布招商信息成功")
        else:
            return output.error_user_defined(driver, "发布招商信息失败，数量没有增加")

    def delete(self, grade=u"省级分销商", **kwargs):
        u'''
        删除招商信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.release_zhaoshang_information_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            num_before = self.get_list_num(self.num)
            driver.find_element_by_xpath\
                (u"//td[text()='%s\n								']/../td[8]/a[text()='删除']"%grade).click()
            time.sleep(1)
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(1)
            driver.switch_to_frame('iframe')
            num_after = self.get_list_num(self.num)
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除招商信息失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_before - num_after):
            return output.pass_user_defined(driver, "删除招商信息成功")
        else:
            return output.error_user_defined(driver, "删除招商信息失败，数量没有减少")


    def release(self, grade=u"省级分销商", **kwargs):
        u'''
        发布招商信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.release_zhaoshang_information_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            num_before = self.get_list_num(self.num)
            driver.find_element_by_xpath\
                (u"//td[text()='%s\n								']/../td[8]/a[text()='发布']"%grade).click()
            time.sleep(1)
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(1)
            driver.switch_to_frame('iframe')
            num_after = self.get_list_num(self.num)
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "发布招商信息失败")
        finally:
            driver.switch_to_default_content()

        if 0 == (num_before - num_after):
            return output.pass_user_defined(driver, "发布招商信息成功")
        else:
            return output.error_user_defined(driver, "发布招商信息失败，数量有变化")

    def close(self, grade=u"省级分销商", **kwargs):
        u'''
        关闭招商信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.release_zhaoshang_information_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            num_before = self.get_list_num(self.num)
            driver.find_element_by_xpath\
                (u"//td[text()='%s\n								']/../td[8]/a[text()='关闭']"%grade).click()
            time.sleep(1)
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            time.sleep(1)
            driver.switch_to_frame('iframe')
            num_after = self.get_list_num(self.num)
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "关闭招商信息失败")
        finally:
            driver.switch_to_default_content()

        if 0 == (num_before - num_after):
            return output.pass_user_defined(driver, "关闭招商信息成功")
        else:
            return output.error_user_defined(driver, "关闭招商信息失败，数量有变化")


    def modify(self, grade=u"省级分销商", **kwargs):
        u'''
        关闭招商信息
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.release_zhaoshang_information_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            num_before = self.get_list_num(self.num)
            driver.find_element_by_xpath\
                (u"//td[text()='%s\n								']/../td[8]/a[text()='修改']"%grade).click()
            time.sleep(1)
            find_element(self.submit).click()
            time.sleep(4)
            num_after = self.get_list_num(self.num)
        except:
            return output.error_user_defined(driver, "修改招商信息失败")
        finally:
            driver.switch_to_default_content()

        if 0 == (num_before - num_after):
            return output.pass_user_defined(driver, "修改招商信息成功")
        else:
            return output.error_user_defined(driver, "修改招商信息失败，数量有变化")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')

    b = EnterpriseReleaseZhaoshangInformation()
    print b.add().msg
    print b.modify().msg
    print b.release().msg
    print b.close().msg
    print b.delete().msg
    #print error.msg