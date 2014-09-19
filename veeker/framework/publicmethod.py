#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from BeautifulSoup import  BeautifulSoup
from framework import setting
import sys
import re
import urllib2
import time
import json

def gethref(page, num, linkname):
    u'''
    @该方法通过输入当前页面的源码 以及订单号 所要查找的链接名，返回最终的链接属性,如下结构的HTML:

    <td width="73" rowspan="1" align="center" class="order_rt">
	<p><a href="javascript:cusOrder.orderDetails('101828509841000237');">订单详情</a></p>
	<p><a href="javascript:cusOrder.delOrder('101828509841000237');">删除</a></p></td>

	<td width="92" valign="middle" class="order_bd">
	<p><a href="javascript:queryOrderReplace(923);">查看退货</a></p>
	<p></p>
	<p><a href="javascript:cusOrder.reviewOrder('923');">评论</a><br /></td>

    @参数结构
    page:页面源码
    num:订单号码
    linkname:所需查找的链接中文名称

    @返回数据
    PASS：返回链接字符串
    FAIL：返回FALSE
    '''
    try:
        href = "javascript:cusOrder.delOrder('"+ num +"');"
        soup = BeautifulSoup(''.join(page))
        a = soup.find("a", {"href":href}).findParent('td').findNextSiblings('td')[0]('a')
        for i in a:
            if i.string == linkname:
                return i['href']
    except:
        return False

    return False


def get_orderpage(text):
    u'''
    该函数用来提取字符串中的数字组，
    如： “共210条，共11页”，提取出来的结果为['210','11']
    :param text: 需要匹配出数字列表的字符串
    :return:匹配结果元组
    '''
    return re.compile(r'\d{1,4}').findall(text)


def modify_host(url):
    u'''
    该函数用于判断一个URL是不是在HOST里，如在则添加进去，HOSTIP 在setting里配置
    用于解决进入商品详情或者商家页面时，因HOST没有配置而没法打开的问题
    :param url:商家商城URL
    :param hostip:WEB服务器IP
    :return:添加结果
    '''
    hostfile = r'C:\Windows\System32\drivers\etc\hosts'
    try:
        with open(hostfile, 'r') as f:
            if url in f.read():
                return True

        with open(hostfile,'a') as f:
            f.write('\n' + setting.HOSTIP + ' ' + url)
    except:
        return False

    return True

def is_element_present(driver, *ele):
    u'''
    该函数用来判断元素是否存在
    :param driver:浏览器对象
    :param ele: 元素定位元组
    :return:判断结果
    '''
    try:
        driver.implicitly_wait(10)
        driver.find_element(*ele)
    except:
        return False
    return True

def is_element_displayed(driver, *ele):
    u'''
    该函数用来判断元素是否可见
    :param driver:浏览器对象
    :param ele:元素定位元组
    :return:判断结果
    '''
    try:
        driver.implicitly_wait(10)
        see = driver.find_element(*ele).is_displayed()
    except:
        return False
    return see

def getvertifycode(towho):
    u'''
    该函数利用mailinator.com的匿名邮件功能收取验证码
    :param towho:邮件地址的ID，不包括后缀
    :return: 1、PASS:验证码  2、FAIL:FALSE
    '''

    time.sleep(10)
    try:
        getidurl = 'https://api.mailinator.com/api/inbox?to=%s&token=a65b978467f54e559c028dff740c9621'%towho
        s = json.loads(str(urllib2.urlopen(getidurl).read()))
        mailurl = 'https://www.mailinator.com/rendermail.jsp?msgid='+s['messages'][0]['id']+'&time='+'1409663495288'
        mail = urllib2.urlopen(mailurl)
        return re.compile(r'\d{6}').search(mail.read()).group()
    except:
        return False

if __name__ == '__main__':
    #print gethref(open('1.html').read(), '101828509841000237', u'评论')
    #print modify_host('www.sunyanhui1.com', '192.168.0.235')
    #print get_orderpage('123我是123我4234')
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    d = webdriver.Chrome()
    logininput = (By.ID, 'userAccount')
    d.get('http://www.company.com')
    print is_element_displayed(d, *logininput)
    d.quit()



