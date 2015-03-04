#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
from common.config import IMGPATH
from element.element_person_goods_bought import ElementGoodsBought
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.action_chains import ActionChains
import traceback,time


class GoodsBought(BasePage, ElementGoodsBought):
    u'''
    新版个人中心已买到的商品页面
    '''

    def returns(self, order,
                reason  = u'商品送错退回',
                describe= u'测试一下下',
                number  = '1',
                picture = os.path.join(IMGPATH, 'logo.jpg'),
                *args, **kwargs):
        u"""
        该方法用于退货
        :param order:订单号码
        :param args:
        :param kwargs:
        :return:
        """
        driver = self.driver
        find_element = self.find_element
        select = self.select_new

        try:
            find_element(self.goods_bought_link).click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[text()='%s']/../../../tr[2]//a[text()='%s']"%(order,u"申请退货")).click()
            find_element(self.return_reason_input).click()
            time.sleep(2)
            ActionChains(driver).move_to_element(self.return_reason_select[1]%reason)
            driver.find_element_by_xpath(self.return_reason_select[1]%reason).click()
            find_element(self.return_describe).send_keys(describe)
            find_element(self.return_number).clear()
            find_element(self.return_number).send_keys(number)
            find_element(self.return_proof).click()
            self.upload_photo(picture)
            find_element(self.submit).click()
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '退货成功~！')

if __name__ == '__main__':
    from action.action_login import Login
    a = GoodsBought()
    b = Login()
    a.open_browser("http://www.wiki110.com")
    b.login('41000000030', '888888')
    print a.returns('103531133941000030')
    import time
    time.sleep(3)
    #a.quit()