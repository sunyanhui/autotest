#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from element.person.obasic_info import *
from common import output
from action.basepage import BasePage
from selenium.webdriver.support.select import Select
import time

class Basic_Info(BasePage):
    def edit(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*basicinfo).click()
            driver.switch_to_frame('iframe')
            sdriver(*realname).clear()
            sdriver(*realname).send_keys(w['realname'])
            if w['sex'] == u'男':
                sdriver(*sexboy).click()
            elif w['sex'] == u'女':
                sdriver(*sexgirl).click()
            else:
                pass
            sdriver(*idcard).clear()
            sdriver(*idcard).send_keys(w['idcard'])
            sdriver(*telephone).clear()
            sdriver(*telephone).send_keys(w['telephone'])
            sdriver(*birthday).send_keys(w['birthday'])
            Select(sdriver(*province)).select_by_visible_text(w['province'])
            Select(sdriver(*city)).select_by_visible_text(w['city'])
            Select(sdriver(*country)).select_by_visible_text(w['country'])
            sdriver(*address).clear()
            sdriver(*address).send_keys(w['address'])
            sdriver(*Button).click()
            driver.switch_to_default_content()
            sdriver(*okButton).click()
            time.sleep(5)
        except:
            return output.error_auto(driver)

        try:
            driver.switch_to_frame('iframe')
            assert sdriver(*realname).get_attribute('value') == w['realname']
            #if w['sex'] == u'男':
            #    print type(sdriver(*sexboy).get_attribute('checked'))
            #    assert sdriver(*sexboy).get_attribute('checked') == True
            #elif w['sex'] == u'女':
            #    assert sdriver(*sexgirl).get_attribute('checked') == True
            #else:
            #    pass
            assert sdriver(*idcard).get_attribute('value') == w['idcard']
            assert sdriver(*telephone).get_attribute('value') == w['telephone']
            #assert sdriver(*province).find_element_by_xpath("//option[@selected='selected']").text == w['province']
            #assert sdriver(*city).find_element_by_xpath("//option[@selected='selected']").text == w['city']
            #assert sdriver(*country).find_element_by_xpath("//option[@selected='selected']").text == w['country']
            assert sdriver(*address).get_attribute('value') == w['address']

            driver.switch_to_default_content()
        except AssertionError:
            return output.error_user_defined(driver, 'save basic info failed')
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, 'save basic info success~!')

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    from action.slogin import Login
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    time.sleep(3)
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    realname='12345678',telephone='15154126587',birthday='1987-02-11',province=u'河南省',
                    city=u'许昌市',country=u'鄢陵县',address='asdlkfjas;dlkjfa;sd',sex=u'男',idcard='411024198702130016',
                    )
    print Login(d).login(**testcase)

    result =  Basic_Info(d).edit(**testcase)
    print result['msg']
    #time.sleep(8)
