#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from element.person.omycenter import *
from element.person.element_order_query import *
from action.basepage import BasePage
from common import output, common
import time
import re


class OrderQuery(BasePage):
    u'''
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

    def if_order_exist(self, orderNumber):
        '''
        判断订单是否存在
        :return:True / False
        '''
        driver = self.driver

        try:
            #点击订单查询链接-切换到iframe-输入商品名称、状态、日期，然后点击搜索
            driver.find_element(*orderQuery).click()
            driver.switch_to_frame('iframe')
        except:
            return output.error_auto(driver)

        if u"订单编号：%s"%orderNumber in driver.page_source:
            driver.switch_to_default_content()
            return output.pass_user_defined(driver, '订单存在')
        else:
            return output.error_user_defined(driver, '订单不存在')

    def confirm_receipt(self, orderNumber):
        u'''
        该方法用于确认收货
        '''

        driver = self.driver
        try:
            #点击订单查询链接，然后切进 iframe
            driver.find_element(*orderQuery).click()
            driver.switch_to_frame('iframe')
            driver.find_element_by_css_selector\
                ('''a[href^="javascript:cusOrder.confirmReceiptOrder('%s"'''%orderNumber).click()
            driver.switch_to_default_content()
            driver.find_element(*okButton).click()
        except:
            return output.error_user_defined(driver, "确认收货失败")
        else:
            return output.pass_user_defined(driver, "确认收货成功")


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
            return output.error_auto(driver)

        try:
            #把所有订单号收集到orderlist列表里
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*stringoforder):
                    orderlist.append(re.compile(r'\d{18}').search(j.text).group())
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        finally:
            driver.switch_to_default_content()

        #如果收集到的情形页面显示的总数不一致，则返回错误
        if len(orderlist)==int(orderpage[0]):
            return output.pass_user_defined(driver, 'order query Success', orderlist=orderlist)
        else:
            return output.error_user_defined(driver, 'order number is error, please check it')

    # def confirm_receipt(self, **w):
    #     u'''
    #     该方法用于确认收货
    #     :param kwargs:订单号码
    #     :return:返回状态
    #     '''
    #
    #     driver = self.driver
    #     sdriver = driver.find_element
    #
    #     try:
    #         #点击订单查询链接，然后切进 iframe
    #         sdriver(*orderQuery).click()
    #         driver.switch_to_frame('iframe')
    #     except:
    #         return output.error_auto(driver)
    #
    #     #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
    #     try:
    #         orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
    #         for i in range(int(orderpage[1])):
    #             for j in driver.find_elements(*confirmreceipt):
    #                 if re.compile(w['ordernumber']).search(j.get_attribute('href')):
    #                     j.click()
    #                     driver.switch_to_default_content()
    #                     sdriver(*okButton).click()
    #                     return output.pass_user_defined(driver, 'confirm receipt success')
    #             if i == (int(orderpage[1])-1):break
    #             sdriver(*nextpage).click()
    #     except:
    #         return output.error_auto(driver)
    #
    #     return output.error_user_defined(driver, 'not fount the order to confirm')


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
            return output.error_auto(driver)


        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*deleteorder):
                    if re.compile(w['ordernumber']).search(j.get_attribute('href')):
                        j.click()
                        driver.switch_to_default_content()
                        sdriver(*okButton).click()
                        return output.pass_user_defined(driver, 'delete order success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not fount the order to delete')

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
            return output.error_auto(driver)

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)
            for i in range(int(orderpage[1])):
                for j in driver.find_elements(*undoorder):
                    if re.compile(w['ordernumber']).search(j.get_attribute('href')):
                        j.click()
                        driver.switch_to_default_content()
                        sdriver(*okButton).click()
                        return output.pass_user_defined(driver, 'undo order success')
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not fount the order to undo')



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
            return output.error_auto(driver)


        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            #获得总页数
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)

            #循环每一页
            for i in range(int(orderpage[1])):

                #找到有删除按钮的一组对象，然后循环判断每个对象，直至找出符合条件的
                for j in driver.find_elements(*deleteorder):

                    #判断其链接中是否包含指定订单号
                    if re.compile(w['ordernumber']).search(j.get_attribute('href')):

                        #根据删除链接定位到申请退货链接，
                        href = common.get_href_review_order(driver.page_source, w['ordernumber'], u'申请退货')

                        #如果href为False，返回没找到订单
                        if href==False:
                            return output.error_user_defined(driver, 'not fount the order to apply')

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
                            driver.switch_to_default_content()
                            return output.pass_user_defined(driver, 'apply return success')
                        else:
                            return output.error_user_defined(driver, 'apply return failed!')

                #判断是否到最后一页，到最后一页则跳出循环
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
                #sdriver(*inputpagenumber).clear()
                #sdriver(*inputpagenumber).send_keys(str(int(i)+2))
                #sdriver(*gobutton).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not fount the order to apply')

    def order_status(self, **w):
        pass

    def review_good(self, **w):
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
            return output.error_auto(driver)

        #遍历所有可以取消的订单，并匹配参数订单号，如匹配则取消
        try:
            #获得总页数
            orderpage = common.get_orderpage(sdriver(*totalpagenumber).text)

            #循环每一页
            for i in range(int(orderpage[1])):

                #找到有删除按钮的一组对象，然后循环判断每个对象，直至找出符合条件的
                for j in driver.find_elements(*deleteorder):

                    #判断其链接中是否包含指定订单号
                    if re.compile(w['ordernumber']).search(j.get_attribute('href')):

                        #根据删除链接定位到申请退货链接，
                        href = common.get_href_review_order(driver.page_source, w['ordernumber'], u'评论')

                        #如果href为False，返回没找到订单
                        if href==False:
                            return output.error_user_defined(driver, 'not fount the order to review')

                        #点击评价-- 填写评价表单，而后提交
                        driver.find_element_by_css_selector('a[href="'+href+'"]').click()
                        if w['reviewgrade'] == u'好评':
                            sdriver(*reviewgrade_01).click()
                        elif w['reviewgrade'] == u'中评':
                            sdriver(*reviewgrade_02).click()
                        elif w['reviewgrade'] == u'差评':
                            sdriver(*reviewgrade_03).clcik()

                        sdriver(*reviewdetail).clear()
                        sdriver(*reviewdetail).send_keys(w['reviewdetail'])

                        if w['ifanonymity'].upper() == 'YES':
                            sdriver(*ifanonymity).click()
                        else:
                            pass

                        sdriver(*Button).click()

                        #判断是否存在‘申请退货已发出’字样，有则返回申请成功
                        driver.switch_to_default_content()
                        driver.implicitly_wait(2)
                        if sdriver(*promptmessage).text == u'评论成功！':
                            sdriver(*okButton).click()
                            return output.pass_user_defined(driver, 'review goods success')
                        else:
                            sdriver(*okButton).click()
                            return output.error_user_defined(driver, 'review goods failed!')

                #判断是否到最后一页，到最后一页则跳出循环
                if i == (int(orderpage[1])-1):break
                sdriver(*nextpage).click()
        except:
            return output.error_auto(driver)

        return output.error_user_defined(driver, 'not fount the order to review')



if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(goodsname='', goodsstatus='', startdate='', enddate='' )
    #testcase = dict(ordernumber='101708787837000237',reviewgrade=u'好评', reviewdetail='1234567890', ifanonymity='YES')
    d.get('http://www.enterprise.com')
    slogin.Login(d).login('15000000237', '888888', '111')
    info = OrderQuery(d)
    #print info.review_good(**testcase)
    #print info.apply_return(**testcase)
    print info.order_query(**testcase)
    #print info.del_address(**testcase)
    time.sleep(3)

    d.quit()
