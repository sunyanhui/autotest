#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from BeautifulSoup import  BeautifulSoup
import sys

def gethref(page, num, linkname):
    u'''
    该方法通过输入当前页面的源码 以及订单号 所要查找的链接名，返回最终的链接属性,如下结构的HTML
    <td width="73" rowspan="1" align="center" class="order_rt">
	<p><a href="javascript:cusOrder.orderDetails('101828509841000237');">订单详情</a></p>
	<p><a href="javascript:cusOrder.delOrder('101828509841000237');">删除</a></p>
		</td>

	<td width="92" valign="middle" class="order_bd">
	<p><a href="javascript:queryOrderReplace(923);">查看退货</a></p>
	<p></p>
	<p><a href="javascript:cusOrder.reviewOrder('923');">评论</a><br />
	    </td>
    :param page:页面源码
    :param num:订单号码
    :param linkname:所需查找的链接中文名称
    :return:链接属性
    '''
    try:
        href = "javascript:cusOrder.delOrder('"+ num +"');"
        soup1 = BeautifulSoup(''.join(page))
        a = soup1.find("a", {"href":href}).findParent('td').findNextSiblings('td')
        soup2 = BeautifulSoup(''.join(str(a)))
        #print soup2
        for i in soup2('a'):
            if i.string == linkname:
                return i['href']
    except:
        return False

    return False



if __name__ == '__main__':
    gethref(open('1.html').read(), '101828509841000237', u'再次购买')

