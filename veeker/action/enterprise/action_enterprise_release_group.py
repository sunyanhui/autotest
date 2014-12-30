#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_enterprise_release_group import ElementReleaseGroup
from action.basepage import BasePage
from common import output

class EnterpriseReleaseGroup(BasePage, ElementReleaseGroup):
    u'''
    企业发布团购商品
    '''

    def release_group(self, goods_type=u'默认分类',goods_name="random", goods_stock="1000",
                      goods_desc="only a test",original_price="999.9", group_price="999.9",
                      start_time='now',end_time='2015-12-30 15:01:11',size='100',**kwargs):
        u'''
        发布商品
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select
        if start_time == 'now':
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        try:
            #点击修改企业发布商品链接，然后切进FRAME
            find_element(self.release_group_link).click()
            driver.switch_to_frame('iframe')
            time.sleep(1)
            select(find_element(self.goods_type),goods_type)
            select(find_element(self.goods_brand), 0)
            if goods_name == "random":
                goods_name = self.creat_random_string()
            find_element(self.goods_name).send_keys(goods_name)
            find_element(self.goods_stock).send_keys(goods_stock)
            find_element(self.original_price).send_keys(original_price)
            find_element(self.group_price).send_keys(group_price)
            js_start="$(\"input[name='describeDTO.groupStartTime']\").removeAttr('readonly');" \
                     "$(\"input[name='describeDTO.groupStartTime']\").attr('value','%s')"%start_time
            driver.execute_script(js_start)

            js_end="$(\"input[name='describeDTO.groupEndTime']\").removeAttr('readonly');" \
                   "$(\"input[name='describeDTO.groupEndTime']\").attr('value','%s')"%end_time
            driver.execute_script(js_end)
            find_element(self.goods_desc).send_keys(goods_desc)
            find_element(self.size).send_keys(size)
            select(find_element(self.select_photo),u'默认分类')
            find_element(self.photo_for_click).click()
            self.insert_html_to_richtext(self.goods_desc_rich[1], goods_desc)
            find_element(self.add).click()
            driver.switch_to_default_content()
            time.sleep(1)
        except:
            return output.error_user_defined(driver, "发布团购商品失败")
        else:
            return output.pass_user_defined(driver, "发布团购商品成功", goods_name=goods_name)

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')
    b = EnterpriseReleaseGroup()
    error = b.release_group()
    print error