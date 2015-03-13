#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_person_modify_password import ElementModifyPassword
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.action_chains import ActionChains
import traceback,time


class PersonModifyPassword(BasePage, ElementModifyPassword):
    u'''
    新版个人中心修改登录密码
    '''

    def modify_password(self,old_password,new_password,repeat_password,*args, **kwargs):
        u"""
        该方法用于修改密码
        :param order:订单号码
        """
        driver = self.driver
        find_element = self.find_element

        try:
            # 把鼠标移动到 “账户设置” 链接上
            ActionChains(driver).move_to_element(find_element(self.account_setting)).perform()
            time.sleep(1)

            # 把鼠标移动到 “密码修改” 链接上，然后点击
            ActionChains(driver).move_to_element(find_element(self.modify_password_link)).click().perform()

            # 输入新旧密码，然后提交
            find_element(self.old_password).send_keys(old_password)
            find_element(self.new_password).send_keys(new_password)
            find_element(self.repeat_password).send_keys(repeat_password)
            find_element(self.submit_button).click()
            time.sleep(1)
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '密码修改成功~！')

if __name__ == '__main__':
    from action.action_login import Login
    a = PersonModifyPassword()
    b = Login()
    a.open_browser("http://www.wiki110.com")
    b.login('41000000024', '888888')
    print a.modify_password('111111','888888','888888').msg
    import time
    time.sleep(3)
    #a.quit()