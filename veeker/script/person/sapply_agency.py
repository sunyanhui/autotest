#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from objectrepository.person.oapply_agency import *
from framework import output, common_method
from framework.output import BreakException
from script.sbase import Base
from selenium import webdriver
from selenium.webdriver.support.select import Select
import traceback
import time

class ApplyAgency(Base):

    def search(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*apply_agency).click()
            driver.switch_to_frame('iframe')
            Select(sdriver(*mode)).select_by_visible_text(w['mode'])
            Select(sdriver(*grade)).select_by_visible_text(w['grade'])
            sdriver(*company_name).clear()
            if not w['companyname'] == '':
                sdriver(*company_name).send_keys(w['companyname'])
            sdriver(*search_button).click()
        except:
            return output.error_auto(driver)

        try:
            orderpage = common_method.get_orderpage(sdriver(*totalpagenumber).text)
        except:
            return output.error_user_defined(driver, "can't find the page")

        return output.pass_user_defined(driver, 'search pass',itemnumber=orderpage[0])


    def search_click(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*apply_agency).click()
            driver.switch_to_frame('iframe')
            Select(sdriver(*mode)).select_by_visible_text(w['mode'])
            Select(sdriver(*grade)).select_by_visible_text(w['grade'])
            sdriver(*company_name).clear()
            if not w['companyname'] == '':
                sdriver(*company_name).send_keys(w['companyname'])
            sdriver(*search_button).click()
        except:
            return output.error_auto(driver)

        try:
            orderpage = common_method.get_orderpage(sdriver(*totalpagenumber).text)
        except:
            return output.error_user_defined(driver, "can't find the page")

        find = False

        try:
            for i in range(int(orderpage[1])):
                applylink = driver.find_elements_by_css_selector(
                    '''input[onclick="apply(%s,01,'%s',%s);"]'''%(w['industryid'], w['enterid'], w['id']))
                if applylink:
                    applylink[0].click()
                    find = True
                    raise BreakException
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except BreakException:
            pass
        except:
            return output.error_auto(driver)

        if find == False:return output.error_user_defined(driver, "can't find the apply link")

        try:
            driver.switch_to_default_content()
            if self.is_element_present(driver,*okButton):
                time.sleep(1)
                sdriver(*okButton).click()
                return output.error_user_defined(driver, "can't not apply, beacause the company are unusual" )
            driver.switch_to_frame('iframe')
            if sdriver(*title).text != u'分销商申请':
                return output.error_user_defined(driver, "open the apply page failed")
            else:
                return output.pass_user_defined(driver, 'open the apply page pass~!')
        except:
            return output.error_auto(driver)


    def apply(self, **w):
        driver = self.driver
        #driver = webdriver.Ie()
        sdriver = driver.find_element

        try:
            sdriver(*agency_account).send_keys(w['agency_account'])
            Select(sdriver(*bank)).select_by_visible_text(w['bank'])
            sdriver(*bank_address).send_keys(w['bank_address'])
            Select(sdriver(*bound_province)).select_by_visible_text(w['bound_province'])
            Select(sdriver(*bound_city)).select_by_visible_text(w['bound_city'])
            sdriver(*remark).send_keys(w['remark'])

            sdriver(*agency_name).send_keys(w['agency_name'])
            sdriver(*agency_address).send_keys((w['agency_address']))
            Select(sdriver(*education)).select_by_visible_text(w['education'])
            sdriver(*weixin).send_keys(w['weixin'])
            imghtml_weixin = self.generate_html(w['weixin_img_path'])
            imghtml_idcard_zm = self.generate_html(w['idcard_zm_img_path'])
            imghtml_idcard_fm = self.generate_html(w['idcard_fm_img_path'])

            driver.execute_script\
                ('''var element= document.getElementById("%s");
                element.innerHTML='%s';'''%(weixin_QR[1], imghtml_weixin))

            driver.execute_script\
                ('''var element= document.getElementById("%s");
                element.innerHTML='%s';'''%(idcard_zm[1], imghtml_idcard_zm))

            driver.execute_script\
                ('''var element= document.getElementById("%s");
                element.innerHTML='%s';'''%(idcard_fm[1], imghtml_idcard_fm))

            sdriver(*submit).click()
        except:
            return output.error_auto(driver)

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    d.get('http://www.company.com')
    testcase = dict(username='15000000393',password='888888',verifycode='1111',ifrememberusername='no',
                    mode=u'全部',grade=u'全部',companyname='',
                    industryid='24',enterid='561',id='263',
                    agency_account='1234567890098765432',bank=u'中国银行',bound_province=u'河南省',bank_address='adsfasdfa',
                    bound_city=u'许昌市',remark='234567890-9876543',agency_name=u'晓晓',agency_address=u'湖北湖北',
                    education=u'本科',weixin='123456',weixin_img_path='d:/Tulips.jpg',
                    idcard_zm_img_path='d:/Tulips.jpg',idcard_fm_img_path='d:/Tulips.jpg',
                    )
    print  slogin.Login(d).login(**testcase)
    info = ApplyAgency(d)
    res =  info.search_click(**testcase)
    cc = info.apply(**testcase)
    print cc['msg']
    time.sleep(10)