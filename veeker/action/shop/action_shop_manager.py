#!/usr/bin/python2.7
#coding=utf-8

import time
from selenium.webdriver.common.by import By
from element.element_shop_manager import ElementManager
from action.basepage import BasePage
from common import output


class ShopManager(BasePage, ElementManager):
    u"""
    联盟店操作员管理
    """

    def add_manager(self, manager_account, **kwargs):
        u'''
        添加操作员
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            # 点击操作员管理链接，切入IFRAME
            find_element(self.manager_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)

            # 点击增加管理员TAB页
            find_element(self.add_manager_tab).click()

            # 输入账号
            find_element(self.manager_account).send_keys(manager_account)

            # 提交
            find_element(self.submit).click()

            # 恢复默认状态
            self.driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "添加管理员失败")
        else:
            return output.pass_user_defined(driver, "添加管理员成功")

    def del_manager(self, manager_account, **kwargs):
        u"""
        删除操作员
        """

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.manager_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)

            #点击账号所在行的删除按钮
            find_element((By.XPATH, "//td[text()='%s']/../td[5]/a[2]"%manager_account)).click()

            #恢复默认状态
            self.driver.switch_to_default_content()
            time.sleep(1)

            #点击确认按钮
            find_element(self.confirm).click()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除管理员失败")
        else:
            return output.pass_user_defined(driver, "删除管理员成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki110.com")
    a.login(username = '31000000001',password = '888888')

    b = ShopManager()
    error = b.add_manager(manager_account ="41000000028")
    b.del_manager(manager_account ="41000000028")
    print error['msg']