#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.person.oapply_shop import *
from common import output
from action.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class ApplyShop(BasePage):

    def apply_shop(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*applyshop).click()
            driver.switch_to_frame('iframe')
            Select(sdriver(*product)).select_by_visible_text(w['product'])
            Select(sdriver(*type)).select_by_visible_text(w['type'])
            Select(sdriver(*province_hezuo)).select_by_visible_text(w['province_hezuo'])
            Select(sdriver(*city_hezuo)).select_by_visible_text(w['city_hezuo'])
            Select(sdriver(*country_hezuo)).select_by_visible_text(w['country_hezuo'])
            sdriver(*entername).clear()
            sdriver(*entername).send_keys(w['entername'])
            sdriver(*linkman).clear()
            sdriver(*linkman).send_keys(w['linkman'])
            sdriver(*phone).clear()
            sdriver(*phone).send_keys(w['phone'])
            sdriver(*weixin).clear()
            sdriver(*weixin).send_keys(w['weixin'])
            sdriver(*qq).clear()
            sdriver(*qq).send_keys(w['qq'])
            sdriver(*email).clear()
            sdriver(*email).send_keys(w['email'])
            Select(sdriver(*province_region)).select_by_visible_text(w['province_region'])
            Select(sdriver(*city_region)).select_by_visible_text(w['city_region'])
            Select(sdriver(*country_region)).select_by_visible_text(w['country_region'])
            sdriver(*address).clear()
            sdriver(*address).send_keys(w['address'])
            sdriver(*remark).clear()
            sdriver(*remark).send_keys(w['remark'])
            sdriver(*submit).click()
        except:
            return output.error_auto()

        try:
            assert sdriver(*title).text == u'开店申请查询'
        except:
            return output.error_auto(driver)
        finally:
            driver.switch_to_default_content()

        return output.pass_user_defined(driver, 'apply shop pass')


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.enterprise.com')
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    product = u'企业分销型网商系统商业版',type = u'商业',province_hezuo=u'河南省',city_hezuo=u'许昌市',
                    country_hezuo=u'鄢陵县',entername=u'无敌小蜜蜂',linkman=u'晓晓',weixin='hgbachgbac',qq='414746010',
                    email='hgbac@qq.com',address='asdfasdfasdfasdfadsf',remark='adfasdfasdf',phone='15154126587',
                    province_region=u'河南省',city_region=u'许昌市',country_region=u'鄢陵县',
                    )
    print  slogin.Login(d).login(**testcase)
    info = ApplyShop(d)
    res =  info.apply_shop(**testcase)
    print res['msg']
    time.sleep(10)
    d.quit()