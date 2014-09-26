#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from objectrepository.person.oaddress import *
from framework import output
from script.page import Page
import time
import re

class InfoCenter(Page):
    u'''
    个人中心 【信息中心】 下相关功能模块
    @1、密码修改
    @2、基本信息修改
    @3、收货地址
    '''

    def add_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()

            #切进收货地址iframe
            driver.switch_to_frame('iframe')

            #切进收货地址管理iframe
            driver.switch_to_frame('iframe')

            #获取‘已保存XX个地址’文字
            addressnumbertext = driver.find_element(*addressNumber).text

            #匹配出数字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group()

            #恢复到默认状态(退回到最初的iframe)
            driver.switch_to_default_content()

            #切进收货地址iframe
            driver.switch_to_frame('iframe')

            #填写表单并提交
            driver.find_element(*province).find_element_by_xpath("//option[@value='"+w['province']+"']").click()
            driver.find_element(*city).find_element_by_xpath("//option[@value='"+w['city']+"']").click()
            driver.find_element(*country).find_element_by_xpath("//option[@value='"+w['country']+"']").click()
            driver.find_element(*addressForMdAd).clear()
            driver.find_element(*addressForMdAd).send_keys(w['address'])
            driver.find_element(*zipCodeForMdAd).clear()
            driver.find_element(*zipCodeForMdAd).send_keys(w['zipcode'])
            driver.find_element(*revicerNameForMdAd).clear()
            driver.find_element(*revicerNameForMdAd).send_keys(w['name'])
            driver.find_element(*mobileForMdAd).clear()
            driver.find_element(*mobileForMdAd).send_keys(w['mobile'])
            driver.find_element(*telephoneForMdAd).clear()
            driver.find_element(*telephoneForMdAd).send_keys(w['telephone'])
            if w['isdefault'].upper() == 'YES':driver.find_element(*isDefaultAddress).click()
            driver.find_element(*Button).click()
            time.sleep(3)

            #获取ADD后收货地址数量
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()

            #恢复到默认状态
            driver.switch_to_default_content()

        except:
            return output.error_auto(driver)

        #判断ADD前后数字变化是否为1，是则ADD 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == 1:
            return output.pass_user_defined(driver, 'Add address Success')
        else:
            return output.error_user_defined(driver,'Add address failed')

    def modify_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()

            #切进收货地址iframe
            driver.switch_to_frame('iframe')

            #切进收货地址管理iframe
            driver.switch_to_frame('iframe')

            #获取‘已保存XX个地址’文字
            addressnumbertext = driver.find_element(*addressNumber).text

            #匹配出数字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group()

            #如果收货地址数量为0，则返回错误
            if numberbefore == 0 :
                return output.error_user_defined(driver, 'No address to modify')
            driver.find_element(*mdaddressLink).click()

            #恢复到默认状态
            driver.switch_to_default_content()
            driver.find_element(*okButton).click()

            #切进收货地址表单iframe
            driver.switch_to_frame('iframe')

            #填写表单并提交
            driver.find_element(*province).find_element_by_xpath("//option[@value='"+w['province']+"']").click()
            driver.find_element(*city).find_element_by_xpath("//option[@value='"+w['city']+"']").click()
            driver.find_element(*country).find_element_by_xpath("//option[@value='"+w['country']+"']").click()
            driver.find_element(*addressForMdAd).clear()
            driver.find_element(*addressForMdAd).send_keys(w['address'])
            driver.find_element(*zipCodeForMdAd).clear()
            driver.find_element(*zipCodeForMdAd).send_keys(w['zipcode'])
            driver.find_element(*revicerNameForMdAd).clear()
            driver.find_element(*revicerNameForMdAd).send_keys(w['name'])
            driver.find_element(*mobileForMdAd).clear()
            driver.find_element(*mobileForMdAd).send_keys(w['mobile'])
            driver.find_element(*telephoneForMdAd).clear()
            driver.find_element(*telephoneForMdAd).send_keys(w['telephone'])
            if w['isdefault'].upper() == 'YES':driver.find_element(*isDefaultAddress).click()
            driver.find_element(*Button).click()
            time.sleep(1)

            #恢复到默认状态
            driver.switch_to_default_content()
            driver.find_element(*okButton).click()

            #获取修改后收货地址数量
            driver.switch_to_frame('iframe')
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()

            #恢复到默认状态
            driver.switch_to_default_content()

        except:
            return output.error_auto(driver)

        #判断MD前后数字变化是否为1，是则ADD 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == 0:
            return output.pass_user_defined(driver, 'Modify address Success')
        else:
            return output.error_user_defined(driver, 'Modify address failed')

    def del_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()

            #切进收货地址iframe
            driver.switch_to_frame('iframe')

            #切进收货地址管理iframe
            driver.switch_to_frame('iframe')

            #获取‘已保存XX个地址’文字
            addressnumbertext = driver.find_element(*addressNumber).text

            #匹配出数字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group()

            if numberbefore == 0 :
                return output.error_user_defined(driver, 'No address to delete')

            driver.find_element(*deladdressLink).click()
            time.sleep(1)

            #恢复到默认状态
            driver.switch_to_default_content()
            driver.find_element(*okButton).click()


            #获取DEL后收货地址数量
            driver.switch_to_frame('iframe')
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()

            #恢复到默认状态
            driver.switch_to_default_content()

        except:
            return output.error_auto(driver)

        #判断DEL前后数字变化是否为-1，是则DEL 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == -1:
            return output.pass_user_defined(driver, 'Delete address Success')
        else:
            return output.error_user_defined(driver, 'Delete address failed')

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    #testcase = dict(province='007041',city='007041001', country='007041001002', address='1234567', zipcode='123456',
     #               name='sunyanhui', mobile='15135417896',telephone='0371-7127556',isdefault='yes' )
    d.get('http://www.company.com')
    print  slogin.Login(d).login('15000000372', '888888', '111')
    info = InfoCenter(d)
    print info.modify_password('888888', '888888', '888888')
    #print info.del_address(**testcase)
    time.sleep(10)

    d.quit()
