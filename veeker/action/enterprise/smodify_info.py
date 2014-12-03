#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from element.enterprise.omodify_info import *
from action.basepage import BasePage
from common import config, output, common
import time, sys



class ModifyInfo(BasePage):

    def modify_info(self, **w):

        driver = self.driver
        driver = webdriver.Ie()
        sdriver = driver.find_element


        try:
            #点击修改企业信息链接，然后切进FRAME
            sdriver(*modify_company_info_link).click()
            driver.switch_to_frame('iframe')

            #输入公司名称
            sdriver(*company_name).clear()
            sdriver(*company_name).send_keys(w['company_name'])

            #输入公司简称
            sdriver(*company_short_name).clear()
            sdriver(*company_short_name).send_keys(w['company_shot_name'])

            #选择经营类型
            Select(sdriver(*operate_type)).select_by_visible_text(w['operate_type'])

            #输入经营范围
            sdriver(*operate_range).clear()
            sdriver(*operate_range).send_keys(w['operate_range'])

            #选择省市县
            Select(sdriver(*province)).select_by_visible_text(w['province'])
            Select(sdriver(*city)).select_by_visible_text(w['city'])
            Select(sdriver(*country)).select_by_visible_text(w['country'])

            #输入详细地址
            sdriver(*address).clear()
            sdriver(*address).send_keys(w['address'])

            #上传商城LOGO
            sdriver(*mall_logo).click()
            time.sleep(1)
            if not self.upload_photo(driver, w['mall_logo']):
                return output.error_user_defined(driver, 'upload mall_logo img failed')
            time.sleep(1)

            #上传商城背景LOGO
            sdriver(*backgroud_logo).click()
            time.sleep(1)
            if not self.upload_photo(driver, w['backgroud_logo']):
                return output.error_user_defined(driver, 'upload backgroud_logo img failed')
            time.sleep(1)

            #输入商城名称
            sdriver(*mall_name).clear()
            sdriver(*mall_name).send_keys(w['mall_name'])

            #输入商城域名
            sdriver(*mall_domain).clear()
            sdriver(*mall_domain).send_keys(w['mall_domain'])

            #输入服务电话
            sdriver(*service_phone).clear()
            sdriver(*service_phone).send_keys(w['service_phone'])

            #输入投诉电话
            sdriver(*complaint_phone).clear()
            sdriver(*complaint_phone).send_keys(w['complaint_phone'])

            #输入备案号
            sdriver(*beianhao).clear()
            sdriver(*beianhao).send_keys(w['beianhao'])

            #输入网络经营许可证
            sdriver(*wangluojingyingxuke).clear()
            sdriver(*wangluojingyingxuke).send_keys(w['wangluojingyingxuke'])

            #输入企业QQ
            sdriver(*company_qq).clear()
            sdriver(*company_qq).send_keys(w['company_qq'])

            #输入网络安全证书
            sdriver(*wangluoanquanzhengshu).clear()
            sdriver(*wangluoanquanzhengshu).send_keys(w['wangluoanquanzhengshu'])

            #输入版权信息
            sdriver(*company_copyright).clear()
            sdriver(*company_copyright).send_keys(w['company_copyright'])

            #上传二维码
            sdriver(*OR_code).click()
            time.sleep(1)
            if not self.upload_photo(driver, w['OR_code']):
                return output.error_user_defined(driver, 'upload OR_code img failed')
            time.sleep(1)

            #上传企业图标
            sdriver(*company_img).click()
            time.sleep(1)
            if not self.upload_photo(driver, w['company_img']):
                return output.error_user_defined(driver, 'upload company_img failed')
            time.sleep(1)

            #提交
            sdriver(*save).click()

            #取得标题
            text = sdriver(*title).text
        except:
            return output.error_auto(driver)
        else:
            if text == u'企业基本信息':
                return output.pass_user_defined(driver, 'save enterprise info pass~!')
            else:
                return output.error_user_defined(driver, 'save enterprise info fail')