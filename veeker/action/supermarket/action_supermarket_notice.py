#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_supermarket_notice import ElementNotice
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.by import By



class SupermarketNotice(BasePage, ElementNotice):
    u'''
    超市公告管理
    '''

    def add_notice(self, title="random",content=u"测试一下", **kwargs):
        u'''
        发布公告
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.notice_manage_link).click()
            driver.switch_to_frame('iframe')
            num_before = self.get_list_num(self.num)

            if title == "random":title = self.creat_random_string()
            find_element(self.add_notice_tab).click()
            find_element(self.title).send_keys(title)
            find_element(self.content).send_keys(content)
            find_element(self.publish).click()
            time.sleep(4)
            num_after = self.get_list_num(self.num)
        except:
            return output.error_user_defined(driver, "发布公告失败")
        finally:
            driver.switch_to_default_content()

        if 1 == (num_after - num_before):
            return output.pass_user_defined(driver, "发布公告成功",title = title)
        else:
            return output.error_user_defined(driver, "发布公告失败，数量没有增加")

    def del_notice(self, title,**kwargs):
        u'''
        删除公告
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.notice_manage_link).click()
            driver.switch_to_frame('iframe')
            num_before = self.get_list_num(self.num)
            find_element((By.XPATH, self.del_link[1]%title)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            driver.switch_to_frame('iframe')
            time.sleep(3)
            num_after = self.get_list_num(self.num)
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
    a.login(username = 'XYHD3100030',password = '888888')

    b = SupermarketNotice()
    error = b.add_notice("123")
    b.del_notice(error.title)
    print error.msg
    print error