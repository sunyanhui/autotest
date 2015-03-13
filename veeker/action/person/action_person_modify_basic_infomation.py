#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_person_modify_basic_infomation import ElementModifyBasicInfomation
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.action_chains import ActionChains
import traceback,time


class PersonModifyBasicInformation(BasePage, ElementModifyBasicInfomation):
    u'''
    新版个人中心修改登录基本信息
    '''

    def modify_basic_information(self,
                                 birthday='1987-02-13',*args, **kwargs):
        u"""
        该方法用于修改基本信息
        """
        driver = self.driver
        find_element = self.find_element

        try:
            # 把鼠标移动到 “账户设置” 链接上
            ActionChains(driver).move_to_element(find_element(self.account_setting)).perform()
            time.sleep(2)
            find_element(self.modify_basic_information_link).click()
            time.sleep(2)
            find_element(self.modify_button).click()

            # 把鼠标移动到 “密码修改” 链接上，然后点击
            #ActionChains(driver).move_to_element(find_element(self.modify_basic_information_link)).click().perform()

            # 输入新旧密码，然后提交
            js_start="$(\"input[name='customerPersonDTO.birthDay']\").removeAttr('readonly');" \
                     "$(\"input[name='customerPersonDTO.birthDay']\").attr('value','%s')"%birthday
            driver.execute_script(js_start)
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '密码修改成功~！')


if __name__ == '__main__':
    from action.action_login import Login
    a = PersonModifyBasicInformation()
    b = Login()
    a.open_browser("http://www.wiki110.com")
    b.login('41000000039', '888888')
    print a.modify_basic_information().msg
    import time
    time.sleep(3)
    #a.quit()