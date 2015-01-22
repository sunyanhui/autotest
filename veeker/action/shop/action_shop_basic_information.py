#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_shop_basic_information import ElementBasicInformation
from action.basepage import BasePage
from common import output
from common.config import IMGPATH
import os
import traceback

class ShopBasicInformation(BasePage, ElementBasicInformation):
    u'''
    联盟店基本信息
    '''

    def test_telephone(self, telephone=''):
        u'''
        验证手机号码输入框
        '''
        return self.__test_input(self.telephone, telephone)

    def test_weixin(self, weixin=''):
        u'''
        验证微信输入框
        '''
        return self.__test_input(self.weixin, weixin)

    def test_location(self, location=''):
        u'''
        验证开户行所在地输入框
        '''
        return self.__test_input(self.opening_bank_location, location)

    def test_agency_account(self, agency_account=''):
        u'''
        验证对公账号输入框
        '''
        return self.__test_input(self.agency_account, agency_account)

    def test_bank_data(self):
        u'''
        验证银行选择下拉框数据
        '''
        try:
            self.find_element(self.basic_information_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.opening_bank_input).click()
            list = self.find_elements(self.opening_bank_list)
            bank_list = []
            for i in list:
                bank_list.append(i.text)
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "获取银行列表成功",bank_list=bank_list )
        finally:
            self.driver.switch_to.default_content()


    def modify(self,telephone = '13123036086',weixin  = '123456',opening_bank_location = u'河南省郑州市',
                 opening_bank =  u'光大银行',img_name = os.path.join(IMGPATH, 'or.jpg')):
        try:
            self.find_element(self.basic_information_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(self.telephone).clear()
            self.find_element(self.telephone).send_keys(telephone)
            self.find_element(self.weixin).clear()
            self.find_element(self.weixin).send_keys(weixin)
            self.find_element(self.opening_bank_location).clear()
            self.find_element(self.opening_bank_location).send_keys(opening_bank_location)
            self.find_element(self.opening_bank_input).click()
            self.driver.find_element_by_xpath(self.opening_bank_list2[1]%opening_bank).click()
            time.sleep(1)
            self.find_element(self.weixin_or).click()
            self.upload_photo(img_name)
            self.find_element(self.submit).click()
            time.sleep(1)
            assert u"修改人员信息成功!" in self.driver.page_source
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver, "基本信息修改成功~！")
        finally:
            self.driver.switch_to.default_content()


    def __test_input(self, element, value):
        u'''
        输入框验证
        :param element:输入框定位元素
        :param value:输入值
        :return:True or False
        '''
        try:
            self.find_element(self.basic_information_link).click()
            self.driver.switch_to.frame("iframe")
            self.find_element(element).clear()
            self.find_element(element).send_keys(value)
            self.find_element(self.form_head).click()
            error_information = self.find_element(self.error_infomation,3).text
        except:
            return output.error_auto(self.driver)
        else:
            return output.pass_user_defined(self.driver,"获取错误信息成功", error_information = error_information)
        finally:
            self.driver.switch_to.default_content()


if __name__ == '__main__':
    import sys, os, time
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from action.action_login import Login

    login = Login()
    login.open_browser("http://www.wiki100.cn")
    login.login("31000000001","888888")
    s = ShopBasicInformation()
    f = s.modify()
    print f.msg
    # a = s.test_telephone()
    # b = s.test_weixin("1")
    # c = s.test_location("")
    # d = s.test_agency_account("1")
    # e = s.test_bank_data()

    # print a.error_information
    # print b.error_information
    # print c.error_information
    # print d.error_information
    # print e.bank_list
    time.sleep(3)
    login.quit()