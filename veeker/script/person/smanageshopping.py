#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.person.omycenter import *
from objectrepository.person.omanageshopping import *
from framework import error, publicmethod
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
     5.apply_return:请求退货
     6.order_status:订单状态
     7.review_good:评价商品


    '''

    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()

    def order_query(self, **w):
        u'''
        该方法用于检查 查询出来的订单总数与实际数是否相等
        :param w: 接收不定参数
        :return:返回状态信息以及订单号列表
        '''

        driver = self.driver
        sdriver = driver.find_element
        orderlist = []

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
            if w['goodsname'] != '':
                sdriver(*goodnameforquery).send_keys(w['goodsname'])
            if w['goodsstatus'] != '':
                sdriver(*goodstatus).find_element_by_xpath("//option[@value='"+w['goodsstatus']+"']").click()
            if w['startdate'] != '':
                sdriver(*startsaledate).send_keys(w['startdate'])
            if w['enddate'] != '':
                sdriver(*endsaledate).send_keys(w['enddate'])
            sdriver(*searchButtonFororder).click()

        except:
            return error.error_auto(driver)


        #建立匹配总订单数与总页数的规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')

        #建立匹配订单号的规则
        pattern2 = re.compile(r'\d{18}')

        try:
            #把所有订单号收集到orderlist列表里
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*stringoforder):
                    orderlist.append(pattern2.search(j.text).group())
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return error.error_auto(driver)

        finally:
            driver.switch_to_default_content()

        #如果收集到的情形页面显示的总数不一致，则返回错误
        if len(orderlist)==int(orderpage[0]):
            return {'result': True, 'orderlist':orderlist, 'describtion': 'order query Success'}
        else:
            return error.error_user_defined(driver, 'order number is error, please check it')

    def confirm_receipt(self, **w):
        u'''
        该方法用于确认收货
        :param kwargs:订单号码
        :return:返回状态
        '''

        driver = self.driver
        sdriver = driver.find_element

        try:
            #点击订单查询链接，然后切进 iframe
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return error.error_auto(driver)

        #建立匹配规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(w['ordernumber'])
        mark = False

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*confirmreceipt):
                    if pattern2.search(j.get_attribute('href')):
                        j.click()
                        driver.switch_to_default_content()
                        sdriver(*okButton).click()
                        mark = True
                        raise error.BreakException()
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except error.BreakException:
            pass
        except:
            return error.error_auto(driver)

        if not mark:
            return error.error_user_defined(driver, 'not fount the order to confirm')

        return {'result': True, 'describtion': 'confirm receipt success'}

    def delete_order(self, **w):
        u'''
        该方法用于删除订单
        :param kwargs:订单号码
        :return:返回取消状态
        '''

        driver = self.driver
        sdriver = driver.find_element

        try:
            #点击订单查询链接，然后切进 iframe
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return error.error_auto(driver)

        #建立匹配规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(w['ordernumber'])
        mark = False

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*deleteorder):
                    if pattern2.search(j.get_attribute('href')):
                        j.click()
                        driver.switch_to_default_content()
                        sdriver(*okButton).click()
                        mark = True
                        raise error.BreakException()
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except error.BreakException:
            pass
        except:
            return error.error_auto(driver)

        if not mark:
            return error.error_user_defined(driver, 'not fount the order to delete')

        return {'result': True, 'describtion': 'delete order success'}

    def undo_order(self, **w):
        u'''
        该方法用于取消订单
        :param kwargs:订单号码
        :return:返回取消状态
        '''

        driver = self.driver
        sdriver = driver.find_element

        try:
            #点击订单查询链接，然后切进 iframe
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return error.error_auto(driver)

        #建立匹配规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(w['ordernumber'])
        mark = False

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*undoorder):
                    if pattern2.search(j.get_attribute('href')):
                        j.click()
                        driver.switch_to_default_content()
                        sdriver(*okButton).click()
                        mark = True
                        raise error.BreakException()
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except error.BreakException:
            pass
        except:
            return error.error_auto(driver)

        if not mark:
            return error.error_user_defined(driver, 'not fount the order to undo')

        return {'result': True, 'describtion': 'undo order success'}

    def apply_return(self, **w):
        u'''
        该方法用于退货
        :param kwargs:订单号码
        :return:返回状态
        '''

        driver = self.driver
        sdriver = driver.find_element

        try:
            #点击订单查询链接，然后切进 iframe
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return error.error_auto(driver)

        #建立匹配规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(w['ordernumber'])

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            #获得总页数
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()

            #循环每一页
            for i in range(int(orderpage[1])):

                #找到有删除按钮的一组对象，然后循环判断每个对象，直至找出符合条件的
                for j in driver.find_elements(*deleteorder):

                    #判断其链接中是否包含指定订单号
                    if pattern2.search(j.get_attribute('href')):

                        #根据删除链接定位到申请退货链接，
                        href = publicmethod.gethref(driver.page_source, w['ordernumber'], u'申请退货')

                        #如果href为False，返回没找到订单
                        if href==False:
                            return error.error_user_defined(driver, 'not fount the order to apply')

                        #点击申请退货-- 填写退货表单，而后提交
                        driver.find_element_by_css_selector('a[href="'+href+'"]').click()
                        sdriver(*returnreason).find_element_by_xpath("//option[@value='"+w['returnreason']+"']").click()
                        sdriver(*returndescription).clear()
                        sdriver(*returndescription).send_keys(w['returndescription'])
                        sdriver(*returnnumber).clear()
                        sdriver(*returnnumber).send_keys(w['returnnumber'])
                        sdriver(*Button).click()

                        #判断是否存在‘申请退货已发出’字样，有则返回申请成功
                        driver.implicitly_wait(5)
                        if u'申请退货已发出' in sdriver(*returnsucceed).text:
                            return {'result': True, 'describtion': 'apply return success'}
                        else:
                            return error.error_user_defined(driver, 'apply return failed!')

                #实现翻页功能，以达到遍历的目的
                if i == (int(orderpage[1])-1):break
                sdriver(*inputpagenumber).clear()
                sdriver(*inputpagenumber).send_keys(str(int(i)+2))
                sdriver(*gobutton).click()
        except:
            return error.error_auto(driver)

        return error.error_user_defined(driver, 'not fount the order to apply')

    def order_status(self, ordernumber=''):
        pass

    def review_good(self, ordernumber='', reviewgrade='', reviewdetail='', ifanonymous='yes',**w):
        u'''
        该方法用于评价商品
        :param kwargs:订单号码
        :return:返回状态
        '''

        driver = self.driver
        sdriver = driver.find_element

        try:
            #点击订单查询链接，然后切进 iframe
            sdriver(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return error.error_auto(driver)

        #建立匹配规则
        pattern1 = re.compile(r'(\d{1,3}).+(\d{1,3})')
        pattern2 = re.compile(w['ordernumber'])

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            #获得总页数
            orderpage = pattern1.search(sdriver(*totalpagenumber).text).groups()

            #循环每一页
            for i in range(int(orderpage[1])):

                #找到有删除按钮的一组对象，然后循环判断每个对象，直至找出符合条件的
                for j in driver.find_elements(*deleteorder):

                    #判断其链接中是否包含指定订单号
                    if pattern2.search(j.get_attribute('href')):

                        #根据删除链接定位到申请退货链接，
                        href = publicmethod.gethref(driver.page_source, w['ordernumber'], u'评价')

                        #如果href为False，返回没找到订单
                        if href==False:
                            return error.error_user_defined(driver, 'not fount the order to review')

                        #点击申请退货-- 填写退货表单，而后提交
                        driver.find_element_by_css_selector('a[href="'+href+'"]').click()
                        sdriver(*returnreason).find_element_by_xpath("//option[@value='"+w['returnreason']+"']").click()
                        sdriver(*returndescription).clear()
                        sdriver(*returndescription).send_keys(w['returndescription'])
                        sdriver(*returnnumber).clear()
                        sdriver(*returnnumber).send_keys(w['returnnumber'])
                        sdriver(*Button).click()

                        #判断是否存在‘申请退货已发出’字样，有则返回申请成功
                        driver.implicitly_wait(5)
                        if u'申请退货已发出' in sdriver(*returnsucceed).text:
                            return {'result': True, 'describtion': 'apply return success'}
                        else:
                            return error.error_user_defined(driver, 'apply return failed!')

                #实现翻页功能，以达到遍历的目的
                if i == (int(orderpage[1])-1):break
                sdriver(*inputpagenumber).clear()
                sdriver(*inputpagenumber).send_keys(str(int(i)+2))
                sdriver(*gobutton).click()
        except:
            return error.error_auto(driver)

        return error.error_user_defined(driver, 'not fount the order to review')



if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    #testcase = dict(goodsname='', goodsstatus='', startdate='', enddate='' )
    testcase = dict(ordernumber='101813556241000237',returnreason='01', returndescription='1234567890', returnnumber='1')
    d.get('http://www.company.com')
    slogin.Login(d).login('15000000237', '888888', '111')
    info = ManageShopping(d)
    print info.apply_return(**testcase)
    #print info.order_query(**testcase)
    #print info.del_address(**testcase)
    time.sleep(3)

    d.quit()
