#!/usr/bin/python2.7
#coding=utf-8

import time
from selenium.webdriver.support.select import Select
from element.element_supermarket_modify_info import ElementModifyInfo
from action.basepage import BasePage
from common import output


class SupermarketModifyInfo(BasePage, ElementModifyInfo):
    u'''
    修改超市基本信息页面对象
    '''

    def modify_info(self,name,shot_name,manage_type,manage_range,province,city,country,
                    address,mall_logo,backgroud_logo,mall_name,domain,service_phone,complaint_phone,
                    bei_an_hao,wang_luo_jing_ying_xu_ke,wang_luo_an_quan_zheng_shu,copyright,
                    OR_code,ico,qq,**kwargs):
        u'''
        修改超市基本信息
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击修改企业信息链接，然后切进FRAME
            find_element(self.modify_supermarket_info_link).click()
            driver.switch_to_frame('iframe')

            #输入公司名称
            find_element(self.supermarket_name).clear()
            find_element(self.supermarket_name).send_keys(name)

            #输入公司简称
            find_element(self.supermarket_short_name).clear()
            find_element(self.supermarket_short_name).send_keys(shot_name)

            #选择经营类型
            Select(find_element(self.operate_type)).select_by_visible_text(manage_type)

            #输入经营范围
            find_element(self.operate_range).clear()
            find_element(self.operate_range).send_keys(manage_range)

            #选择省市县
            Select(find_element(self.province)).select_by_visible_text(province)
            Select(find_element(self.city)).select_by_visible_text(city)
            Select(find_element(self.country)).select_by_visible_text(country)

            #输入详细地址
            find_element(self.address).clear()
            find_element(self.address).send_keys(address)

            #上传商城LOGO
            find_element(self.mall_logo).click()
            time.sleep(1)
            if not self.upload_photo(mall_logo):
                return output.error_user_defined(driver, '上传商城logo失败')
            time.sleep(1)

            #上传商城背景LOGO
            find_element(self.backgroud_logo).click()
            time.sleep(1)
            if not self.upload_photo(backgroud_logo):
                return output.error_user_defined(driver, '上传后台LOGO失败')
            time.sleep(1)

            #输入商城名称
            find_element(self.mall_name).clear()
            find_element(self.mall_name).send_keys(mall_name)

            #输入商城域名
            find_element(self.mall_domain).clear()
            find_element(self.mall_domain).send_keys(domain)

            #输入服务电话
            find_element(self.service_phone).clear()
            find_element(self.service_phone).send_keys(service_phone)

            #输入投诉电话
            find_element(self.complaint_phone).clear()
            find_element(self.complaint_phone).send_keys(complaint_phone)

            #输入备案号
            find_element(self.beianhao).clear()
            find_element(self.beianhao).send_keys(bei_an_hao)

            #输入网络经营许可证
            find_element(self.wangluojingyingxuke).clear()
            find_element(self.wangluojingyingxuke).send_keys(wang_luo_jing_ying_xu_ke)

            #输入企业QQ
            find_element(self.qq).clear()
            find_element(self.qq).send_keys(qq)

            #输入网络安全证书
            find_element(self.wangluoanquanzhengshu).clear()
            find_element(self.wangluoanquanzhengshu).send_keys(wang_luo_an_quan_zheng_shu)

            #输入版权信息
            find_element(self.copyright).clear()
            find_element(self.copyright).send_keys(copyright)

            #上传二维码
            find_element(self.OR_code).click()
            time.sleep(1)
            if not self.upload_photo(OR_code):
                return output.error_user_defined(driver, '上传OR_code失败')
            time.sleep(1)

            #上传企业图标
            find_element(self.ico).click()
            time.sleep(1)
            if not self.upload_photo(ico):
                return output.error_user_defined(driver, '上传超市图标失败')
            time.sleep(1)

            #提交
            find_element(self.save).click()

            #取得标题
            text = find_element(self.title).text
        except:
            return output.error_auto(driver)
        else:
            if text == u'超市基本信息':
                return output.pass_user_defined(driver, 'save enterprise info pass~!')
            else:
                return output.error_user_defined(driver, 'save enterprise info fail')