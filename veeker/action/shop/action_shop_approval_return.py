#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.element_shop_approval_return import ElementApprovalReturn
from action.basepage import BasePage
from common import output
from selenium.webdriver.common.by import By

class ShopApprovalReturn(BasePage, ElementApprovalReturn):
    u'''
    联盟店审批客户退货
    '''

    def approval(self, order,approval_option=u'通过',approval_comments=u'测试一下下', *args, **kwargs):
        u"""
        通过订单号码去审批
        :param orderNumber:订单号码
        :return:True / False
        """
        driver = self.driver
        find_element = self.find_element
        approval_link = (By.XPATH,u"//span[text()='%s']/../../../tr[2]//a[text()='%s']"%(order,u"审批"))

        try:
            # 点击订单查询链接-切换到iframe-输入订单编号，然后点击搜索
            find_element(self.approval_return_link).click()
            driver.switch_to_frame('iframe')
            find_element(approval_link, 2).click()
            if approval_option == u'通过':
                find_element(self.approval_by).click()
            else:
                find_element(self.approval_turn_down).click()

            find_element(self.approval_comments).send_keys(approval_comments)
            find_element(self.submit).click()
            assert u'审批成功' in driver.page_source
        except:
            return output.error_auto(driver)
        else:
            return output.pass_user_defined(driver, '发货成功~！')
        finally:
            driver.switch_to_default_content()


if __name__ == '__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki110.com")
    a.login('31000000001', '888888')

    b = ShopApprovalReturn()
    print b.approval('103547502241000030')

    import time
    time.sleep(3)
    b.quit()
