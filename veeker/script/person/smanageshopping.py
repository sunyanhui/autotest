#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from selenium import webdriver
from objectrepository.person.omycenter import *
from objectrepository.person.omanageshopping import *
from framework import error
import time
import re


class ManageShopping():
    '''
    该类集成了购物管理下相关操作
    @订单查询
     1.order_query:订单查询
     2.confirm_receipt:确认收货
     3.delete_order:删除订单
     4.undo_order:撤销订单
     5.apply_for_return:请求退货
     6.order_status:订单状态
     7.review_good:评价商品


    '''

    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()

    def order_query(self, gname='', gstatus='', sdate='', edate='',**kwgs):

        driver = self.driver
        sdriver = driver.find_element
        orderlist = []

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
            if gname != '':
                sdriver(*goodnameforquery).send_keys(gname)
            if gstatus != '':
                sdriver(*goodstatus).find_element_by_xpath("//option[@value='"+gstatus+"']").click()
            if sdate != '':
                sdriver(*startsaledate).send_keys(sdate)
            if edate != '':
                sdriver(*endsaledate).send_keys(edate)
            sdriver(*searchButtonFororder).click()

        except:
            return error.error_auto(driver)



        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(r'\d{18}')

        orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()

        for i in range(int(orderpage[1])):

            for j in driver.find_elements(*stringoforder):
                orderlist.append(pattern2.search(j.text).group())
            if i == int(orderpage[1]):break
            sdriver(*nextpage).click()

        print orderlist
        print len(orderlist)



    def confirm_receipt(self, ordernumber=''):
        pass

    def delete_order(self, ordernumber=''):
        pass

    def undo_order(self, ordernumber=''):
        pass

    def apply_for_return(self, ordernumber='', returnreason='', returndescribtion='', returnnumber='', **kwgs):
        pass

    def order_status(self, ordernumber=''):
        pass

    def review_good(self, ordernumber='', reviewgrade='', reviewdetail='', ifanonymous='yes',**w):
        pass


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(gname='', gstatus='', sdate='', edate='' )
    d.get('http://www.company.com')
    slogin.Login(d).login('15000000237', '888888', '111')
    info = ManageShopping(d)
    print info.order_query(**testcase)
    #print info.del_address(**testcase)
    time.sleep(3)

    d.quit()
