#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import time
import re
from element.element_person_apply_shop import ElementApplyShop
from action.basepage import BasePage
from common import output, common


class ApplyShop(BasePage, ElementApplyShop):
    u'''

    '''

    def apply(self,mode=u"采购代理", *args, **kwargs):
        '''
        '''
        driver = self.driver
        find_element = self.find_element
        select = self.select_new

        try:
            find_element(self.apply_shop_link).click()
            select(self.mode, mode)
            find_element(self.supermarket_name).send_keys()
            find_element(self.apply_btn).click()

        except:
            pass

if __name__ == '__main__':
    pass