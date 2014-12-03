#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
import smtplib
import re
import urllib2
import logging

def send_mail(file_path, tolist):
    u'''
    @该函数用来在测试完成后发送测试报告
    file_path: 报告完整路径
    tolist:   接收邮件列表 可以使用setting.REPORTTOLIST参数的设置
    '''
    msg = MIMEMultipart()
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=%s'%file_path.split("\\")[-1]
    msg.attach(att1)
    msg['from'] = 'hgbac@163.com'
    msg['to'] = 'hgbac@163.com'
    msg['Subject'] = u'测试报告'

    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login('hgbac','hgbac123abc')
        server.sendmail(msg['from'], tolist, msg.as_string())
        logging.info(u'邮件发送成功~!')
        server.quit()
        return True
    except:
        logging.error(u'邮件发送失败~!')
        return False



def get_href_review_order(page, num, linkname):
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

def get_href_undo_myfavorite(page, onclick, linkname):

    try:
        soup = BeautifulSoup(''.join(page))
        a = soup.find("a", {'onclick':onclick.rstrip(),'class':'jrgw'}).findParent('td')('a')[1]
        if a.string == linkname:
            return a['href']
        else:
            return False
    except:
        return False

def get_orderpage(text):
    u'''
    @该函数用来提取字符串中的数字组，
    如： “共210条，共11页”，提取出来的结果为['210','11']

    @参数
    text: 需要匹配出数字列表的字符串

    @返回数据
    返回匹配结果元组
    '''
    return re.compile(r'\d{1,4}').findall(text)


def modify_host(url):
    u'''
    @该函数用于判断一个URL是不是在HOST里，如在则添加进去，HOSTIP 在setting里配置
    用于解决进入商品详情或者商家页面时，因HOST没有配置而没法打开的问题

    @参数
    url:商家商城URL
    hostip:WEB服务器IP

    @返回数据
    添加状态
    '''
    hostfile = r'C:\Windows\System32\drivers\etc\hosts'
    try:
        with open(hostfile, 'r') as f:
            if url in f.read():
                return True

        with open(hostfile,'a') as f:
            f.write('\n' + config.HOSTIP + ' ' + url)
    except:
        return False

    return True

def is_element_present(driver, *ele):
    u'''
    @该函数用来判断元素是否存在

    @参数
    driver:浏览器对象
    ele: 元素定位元组

    @返回数据
    返回判断结果 True False
    '''
    try:
        driver.implicitly_wait(10)
        driver.find_element(*ele)
    except:
        return False
    return True

def is_element_displayed(driver, *ele):
    u'''
    @该函数用来判断元素是否可见

    @参数
    driver:浏览器对象
    ele:元素定位元组

    @返回数据
    返回判断结果
    '''
    try:
        driver.implicitly_wait(10)
        see = driver.find_element(*ele).is_displayed()
    except:
        return False
    return see

def getvertifycode(towho):

    try:
        r = urllib2.urlopen('http://mailcatch.com/en/temporary-inbox?box=%s'%towho)
        soup = BeautifulSoup(r.read())
        id= soup.find('input', id='first_mail_id')['value']
        mail = urllib2.urlopen('http://mailcatch.com/en/temporary-mail-content?box=%s=mailcatch.com=mailcatch.com&show=%s'%(towho,id))
        return re.compile(r'\d{6}').search(mail.read()).group()
    except:
        return False

if __name__ == '__main__':
    #print gethref(open('1.html').read(), '101828509841000237', u'评论')
    #print modify_host('www.sunyanhui1.com', '192.168.0.235')
    #print get_orderpage('123我是123我4234')

    #from selenium import webdriver
    #from selenium.webdriver.common.by import By
    #d = webdriver.Chrome()
    #logininput = (By.ID, 'userAccount')
    #d.get('http://www.enterprise.com')
    #print is_element_displayed(d, *logininput)
    #d.quit()
    send_mail(r'D:\autotest\veeker\result\result_2014-12-02-10_53_49.html', ['hgbac@qq.com', 'sunyanhui@foxmail.com'])



