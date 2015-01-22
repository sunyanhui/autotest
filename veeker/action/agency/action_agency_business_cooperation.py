#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_agency_business_cooperation import ElementBusinessCooperation
from action.basepage import BasePage
from common import output

class AgencyBusinessCooperation(BasePage, ElementBusinessCooperation):
    u'''
    分销商合作商家
    '''

    def test_alliance_status(self):
        u'''
        验证联盟状态下拉框数据
        返回:alliance_status_list列表
        '''
        try:
            self.find_element(self.business_cooperation_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.alliance_status).click()
            list = self.find_elements(self.alliance_status_list)
            alliance_status_list = []
            for i in list:
                alliance_status_list.append(i.text.rstrip())
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "获取联盟状态成功",alliance_status_list=alliance_status_list )
        finally:
            self.driver.switch_to.default_content()

    def search(self, company='',alliance_status=u'已绑定'):
        u'''
        合作商家搜索脚本
        '''
        try:
            self.find_element(self.business_cooperation_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.alliance_enterprise_input).send_keys(company)
            self.find_element(self.alliance_status).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(u"//li[contains(text(),'%s')]"%alliance_status).click()
            self.find_element(self.search_button).click()
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "搜索成功")
        finally:
            self.driver.switch_to.default_content()


if __name__ == '__main__':
    import sys, os, time
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("41000000020","888888")
    s = AgencyBusinessCooperation()
    a = s.test_alliance_status()
    print a.alliance_status_list
    b = s.search()
    print b.msg
    time.sleep(3)
    s.quit()