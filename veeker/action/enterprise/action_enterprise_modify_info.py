#!/usr/bin/python2.7
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from element.enterprise.element_enterprise_modify_info import *
from action.basepage import BasePage
from common import output
import time

class EnterpriseModifyInfo(BasePage):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_info(self, **w):
        u'''
        修改超市基本信息
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(modify_enterprise_info_link).click()
            driver.switch_to_frame('iframe')

            #输入公司名称
            find_element(enterprise_name).clear()
            find_element(enterprise_name).send_keys(w['name'])

            #输入公司简称
            find_element(enterprise_short_name).clear()
            find_element(enterprise_short_name).send_keys(w['shot_name'])

            #选择经营类型
            Select(find_element(operate_type)).select_by_visible_text(w['manage_type'])

            #输入经营范围
            find_element(operate_range).clear()
            find_element(operate_range).send_keys(w['manage_range'])

            #选择省市县
            Select(find_element(province)).select_by_visible_text(w['province'])
            Select(find_element(city)).select_by_visible_text(w['city'])
            Select(find_element(country)).select_by_visible_text(w['country'])

            #输入详细地址
            find_element(address).clear()
            find_element(address).send_keys(w['address'])

            #上传商城LOGO
            find_element(mall_logo).click()
            time.sleep(1)
            if not self.upload_photo(w['mall_logo']):
                return output.error_user_defined(driver, '上传商城logo失败')
            time.sleep(1)

            #上传商城背景LOGO
            find_element(backgroud_logo).click()
            time.sleep(1)
            if not self.upload_photo(w['backgroud_logo']):
                return output.error_user_defined(driver, '上传后台LOGO失败')
            time.sleep(1)

            #输入商城名称
            find_element(mall_name).clear()
            find_element(mall_name).send_keys(w['mall_name'])

            #输入商城域名
            find_element(mall_domain).clear()
            find_element(mall_domain).send_keys(w['domain'])

            #输入服务电话
            find_element(service_phone).clear()
            find_element(service_phone).send_keys(w['service_phone'])

            #输入投诉电话
            find_element(complaint_phone).clear()
            find_element(complaint_phone).send_keys(w['complaint_phone'])

            #输入备案号
            find_element(beianhao).clear()
            find_element(beianhao).send_keys(w['bei_an_hao'])

            #输入网络经营许可证
            find_element(wangluojingyingxuke).clear()
            find_element(wangluojingyingxuke).send_keys(w['wang_luo_jing_ying_xu_ke'])

            #输入企业QQ
            find_element(qq).clear()
            find_element(qq).send_keys(w['qq'])

            #输入网络安全证书
            find_element(wangluoanquanzhengshu).clear()
            find_element(wangluoanquanzhengshu).send_keys(w['wang_luo_an_quan_zheng_shu'])

            #输入版权信息
            find_element(copyright).clear()
            find_element(copyright).send_keys(w['copyright'])

            #上传二维码
            find_element(OR_code).click()
            time.sleep(1)
            if not self.upload_photo(w['OR_code']):
                return output.error_user_defined(driver, '上传OR_code失败')
            time.sleep(1)

            #上传企业图标
            find_element(ico).click()
            time.sleep(1)
            if not self.upload_photo(w['ico']):
                return output.error_user_defined(driver, '上传超市图标失败')
            time.sleep(1)

            #提交
            find_element(save).click()

            #取得标题
            text = find_element(title).text
        except:
            return output.error_auto(driver)
        else:
            if text == u'企业基本信息':
                return output.pass_user_defined(driver, '保存企业基本信息成功!')
            else:
                return output.error_user_defined(driver, '保存企业基本信息失败')