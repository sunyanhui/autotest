#!/usr/bin/python2.7
#coding=utf-8

import time
from selenium.webdriver.common.by import By
from element.element_agency_role import ElementRole
from action.basepage import BasePage
from common import output


class AgencyRole(BasePage, ElementRole):
    u"""
    分销商角色管理
    """

    def add_role(self, role_name='tester', *args, **kwargs):
        u"""
        添加角色
        """

        driver = self.driver
        find_element = self.find_element

        try:
            # 点击角色管理链接
            find_element(self.role_link).click()

            # 切入IFRAME
            driver.switch_to_frame('iframe')
            time.sleep(1)

            # 点击增加角色TAB
            find_element(self.add_role_tab).click()

            # 输入角色名
            find_element(self.role_name).send_keys(role_name)

            # 勾选所需权限
            find_element(self.info).click()

            # 提交
            find_element(self.submit).click()

            # 恢复默认状态
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "添加角色失败")
        else:
            return output.pass_user_defined(driver, "添加角色成功")

    def del_role(self, role_name='tester',**kwargs):
        u"""
        删除角色
        """

        driver = self.driver
        find_element = self.find_element

        try:
            # 点击角色管理链接
            find_element(self.role_link).click()

            # 切入IFRAME
            driver.switch_to_frame('iframe')
            time.sleep(1)


            find_element((By.XPATH, "//span[text()='%s']/../../td[3]/a[2]" % role_name)).click()
            driver.switch_to_default_content()
            time.sleep(1)
            find_element(self.confirm).click()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "删除角色失败")
        else:
            return output.pass_user_defined(driver, "删除角色成功")

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki110.com")
    a.login(username = '41000000002',password = '888888')

    b = AgencyRole()
    error = b.del_role(role_name ="tester")
    print error['msg']