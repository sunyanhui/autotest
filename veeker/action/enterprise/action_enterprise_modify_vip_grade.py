#!/usr/bin/python2.7
#coding=utf-8

import time

from element.element_enterprise_modify_vip_grade import ElementModifyVipGrade
from action.basepage import BasePage
from common import output


class EnterpriseModifyVipGrade(BasePage, ElementModifyVipGrade):
    u'''
    修改企业会员等级
    '''

    def modify_vip_grade(self,
        lingshou_totalcash = "1000",lingshou_discount = "90",lingshou_reason = u"测试一下",
        youhui_totalcash   = "2000",youhui_discount   = "80",youhui_reason   = u"测试一下",
        yinpai_totalcash   = "3000",yinpai_discount   = "70",yinpai_reason   = u"测试一下",
        jinpai_totalcash   = "4000",jinpai_discount   = "60",jinpai_reason   = u"测试一下",
        zhuanshi_totalcash = "5000",zhuanshi_discount = "50",zhuanshi_reason = u"测试一下",
        guibin_totalcash   = "6000",guibin_discount   = "40",guibin_reason   = u"测试一下",
        **kwargs):
        u'''
        修改企业会员等级
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击企业会员等级链接，然后切进FRAME
            find_element(self.vip_grade).click()
            driver.switch_to_frame('iframe')
            find_element(self.modify).click()

            #零售会员
            find_element(self.lingshou_totalcash).clear()
            find_element(self.lingshou_totalcash).send_keys(lingshou_totalcash)
            find_element(self.lingshou_discount).clear()
            find_element(self.lingshou_discount).send_keys(lingshou_discount)
            find_element(self.lingshou_reason).clear()
            find_element(self.lingshou_reason).send_keys(lingshou_reason)

            #优惠会员
            find_element(self.youhui_totalcash).clear()
            find_element(self.youhui_totalcash).send_keys(youhui_totalcash)
            find_element(self.youhui_discount).clear()
            find_element(self.youhui_discount).send_keys(youhui_discount)
            find_element(self.youhui_reason).clear()
            find_element(self.youhui_reason).send_keys(youhui_reason)

            #银牌会员
            find_element(self.yinpai_totalcash).clear()
            find_element(self.yinpai_totalcash).send_keys(yinpai_totalcash)
            find_element(self.yinpai_discount).clear()
            find_element(self.yinpai_discount).send_keys(yinpai_discount)
            find_element(self.yinpai_reason).clear()
            find_element(self.yinpai_reason).send_keys(yinpai_reason)

            #金牌会员
            find_element(self.jinpai_totalcash).clear()
            find_element(self.jinpai_totalcash).send_keys(jinpai_totalcash)
            find_element(self.jinpai_discount).clear()
            find_element(self.jinpai_discount).send_keys(jinpai_discount)
            find_element(self.jinpai_reason).clear()
            find_element(self.jinpai_reason).send_keys(jinpai_reason)

            #钻石会员
            find_element(self.zhuanshi_totalcash).clear()
            find_element(self.zhuanshi_totalcash).send_keys(zhuanshi_totalcash)
            find_element(self.zhuanshi_discount).clear()
            find_element(self.zhuanshi_discount).send_keys(zhuanshi_discount)
            find_element(self.zhuanshi_reason).clear()
            find_element(self.zhuanshi_reason).send_keys(zhuanshi_reason)

            #贵宾会员
            find_element(self.guibin_totalcash).clear()
            find_element(self.guibin_totalcash).send_keys(guibin_totalcash)
            find_element(self.guibin_discount).clear()
            find_element(self.guibin_discount).send_keys(guibin_discount)
            find_element(self.guibin_reason).clear()
            find_element(self.guibin_reason).send_keys(guibin_reason)

            find_element(self.submit).click()
            time.sleep(4)
        except:

            driver.switch_to_default_content()
            return output.error_user_defined(driver, "修改会员等级失败")
        else:
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "修改会员等级成功")