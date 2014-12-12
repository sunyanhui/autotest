#!/usr/bin/python2.7
#coding=utf-8

from element.enterprise.element_enterprise_modify_vip_grade import *
from action.basepage import BasePage
from common import output
import time

class EnterpriseModifyVipGrade(BasePage):
    u'''
    修改企业会员等级
    '''

    def modify_vip_grade(self, **w):
        u'''
        修改企业会员等级
        '''

        driver = self.driver
        find_element = self.find_element

        try:
            #点击企业会员等级链接，然后切进FRAME
            find_element(vip_grade).click()
            driver.switch_to_frame('iframe')
            find_element(modify).click()

            #零售会员
            find_element(lingshou_totalcash).clear()
            find_element(lingshou_totalcash).send_keys(w['lingshou_totalcash'])
            find_element(lingshou_discount).clear()
            find_element(lingshou_discount).send_keys(w['lingshou_discount'])
            find_element(lingshou_reason).clear()
            find_element(lingshou_reason).send_keys(w['lingshou_reason'])

            #优惠会员
            find_element(youhui_totalcash).clear()
            find_element(youhui_totalcash).send_keys(w['youhui_totalcash'])
            find_element(youhui_discount).clear()
            find_element(youhui_discount).send_keys(w['youhui_discount'])
            find_element(youhui_reason).clear()
            find_element(youhui_reason).send_keys(w['youhui_reason'])

            #银牌会员
            find_element(yinpai_totalcash).clear()
            find_element(yinpai_totalcash).send_keys(w['yinpai_totalcash'])
            find_element(yinpai_discount).clear()
            find_element(yinpai_discount).send_keys(w['yinpai_discount'])
            find_element(yinpai_reason).clear()
            find_element(yinpai_reason).send_keys(w['yinpai_reason'])

            #金牌会员
            find_element(jinpai_totalcash).clear()
            find_element(jinpai_totalcash).send_keys(w['jinpai_totalcash'])
            find_element(jinpai_discount).clear()
            find_element(jinpai_discount).send_keys(w['jinpai_discount'])
            find_element(jinpai_reason).clear()
            find_element(jinpai_reason).send_keys(w['jinpai_reason'])

            #钻石会员
            find_element(zhuanshi_totalcash).clear()
            find_element(zhuanshi_totalcash).send_keys(w['zhuanshi_totalcash'])
            find_element(zhuanshi_discount).clear()
            find_element(zhuanshi_discount).send_keys(w['zhuanshi_discount'])
            find_element(zhuanshi_reason).clear()
            find_element(zhuanshi_reason).send_keys(w['zhuanshi_reason'])

            #贵宾会员
            find_element(guibin_totalcash).clear()
            find_element(guibin_totalcash).send_keys(w['guibin_totalcash'])
            find_element(guibin_discount).clear()
            find_element(guibin_discount).send_keys(w['guibin_discount'])
            find_element(guibin_reason).clear()
            find_element(guibin_reason).send_keys(w['guibin_reason'])

            find_element(submit).click()
            time.sleep(4)
        except:
            return output.error_user_defined(driver, "修改会员等级失败")
        else:
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, "修改会员等级成功")