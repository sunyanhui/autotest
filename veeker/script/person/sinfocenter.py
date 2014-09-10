#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.person.omycenter import *
from framework import setting
import time
import re

class InfoCenter():
    u'''
    个人中心 【信息中心】 下相关功能模块
    @1、密码修改
    @2、基本信息修改
    @3、收货地址
    '''

    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Ie()


    def modify_password(self, o, n ,c):

        driver = self.driver

        try:
            driver.find_element(modifyPassword[0], modifyPassword[1]).click()
            driver.switch_to_frame('iframe')
            driver.find_element(oldPasswordInput[0], oldPasswordInput[1]).clear()
            driver.find_element(oldPasswordInput[0], oldPasswordInput[1]).send_keys(o)
            driver.find_element(newPasswordInput[0], newPasswordInput[1]).clear()
            driver.find_element(newPasswordInput[0], newPasswordInput[1]).send_keys(n)
            driver.find_element(confirmPasswordInput[0], confirmPasswordInput[1]).clear()
            driver.find_element(confirmPasswordInput[0], confirmPasswordInput[1]).send_keys(c)
            driver.find_element(passwordSubmit[0], passwordSubmit[1]).click()

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': sys.exc_info()[1],
                    'errorimg': imgpath
            }


    def add_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()
            driver.switch_to_frame('iframe') #切进收货地址iframe

            #获取ADD前收货地址数量
            driver.switch_to_frame('iframe') #切进收货地址管理iframe
            addressnumbertext = driver.find_element(*addressNumber).text #获取‘已保存XX个地址’文字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group() #匹配出数字

            driver.switch_to_default_content() #恢复到默认状态
            driver.switch_to_frame('iframe') #切进收货地址iframe

            #填写表单并提交
            driver.find_element(*province).find_element_by_xpath("//option[@value='"+w['province']+"']").click()
            driver.find_element(*city).find_element_by_xpath("//option[@value='"+w['city']+"']").click()
            driver.find_element(*country).find_element_by_xpath("//option[@value='"+w['country']+"']").click()
            driver.find_element(*addressForMdAd).clear()
            driver.find_element(*addressForMdAd).send_keys(w['address'])
            driver.find_element(*zipCodeForMdAd).clear()
            driver.find_element(*zipCodeForMdAd).send_keys(w['zipcode'])
            driver.find_element(*revicerNameForMdAd).clear()
            driver.find_element(*revicerNameForMdAd).send_keys(w['name'])
            driver.find_element(*mobileForMdAd).clear()
            driver.find_element(*mobileForMdAd).send_keys(w['mobile'])
            driver.find_element(*telephoneForMdAd).clear()
            driver.find_element(*telephoneForMdAd).send_keys(w['telephone'])
            if w['isdefault'].upper() == 'YES':driver.find_element(*isDefaultAddress).click()
            driver.find_element(*Button).click()
            time.sleep(3)

            #获取ADD后收货地址数量
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()
            driver.switch_to_default_content() #恢复到默认状态

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': sys.exc_info()[1],
                    'errorimg': imgpath
            }

        #判断ADD前后数字变化是否为1，是则ADD 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == 1:
            return {'result': True,
                    'describtion': 'Add address Success',
            }

        else:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': 'Add address failed',
                    'errorimg': imgpath
            }

    def modify_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()
            driver.switch_to_frame('iframe') #切进收货地址iframe

            #获取MD前收货地址数量
            driver.switch_to_frame('iframe') #切进收货地址管理iframe
            addressnumbertext = driver.find_element(*addressNumber).text #获取‘已保存XX个地址’文字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group() #匹配出数字

            if numberbefore == 0 :
                imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
                driver.get_screenshot_as_file(imgpath)
                return {'result': False,
                        'describtion': 'No address to modify',
                        'errorimg': imgpath
                }

            driver.find_element(*mdaddressLink).click()
            driver.switch_to_default_content() #恢复到默认状态
            driver.find_element(*okButton).click()
            driver.switch_to_frame('iframe') #切进收货地址表单iframe

            #填写表单并提交
            driver.find_element(*province).find_element_by_xpath("//option[@value='"+w['province']+"']").click()
            driver.find_element(*city).find_element_by_xpath("//option[@value='"+w['city']+"']").click()
            driver.find_element(*country).find_element_by_xpath("//option[@value='"+w['country']+"']").click()
            driver.find_element(*addressForMdAd).clear()
            driver.find_element(*addressForMdAd).send_keys(w['address'])
            driver.find_element(*zipCodeForMdAd).clear()
            driver.find_element(*zipCodeForMdAd).send_keys(w['zipcode'])
            driver.find_element(*revicerNameForMdAd).clear()
            driver.find_element(*revicerNameForMdAd).send_keys(w['name'])
            driver.find_element(*mobileForMdAd).clear()
            driver.find_element(*mobileForMdAd).send_keys(w['mobile'])
            driver.find_element(*telephoneForMdAd).clear()
            driver.find_element(*telephoneForMdAd).send_keys(w['telephone'])
            if w['isdefault'].upper() == 'YES':driver.find_element(*isDefaultAddress).click()
            driver.find_element(*Button).click()
            time.sleep(1)
            driver.switch_to_default_content() #恢复到默认状态
            driver.find_element(*okButton).click()

            #获取MD后收货地址数量
            driver.switch_to_frame('iframe')
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()
            driver.switch_to_default_content() #恢复到默认状态

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': sys.exc_info()[1],
                    'errorimg': imgpath
            }

        #判断MD前后数字变化是否为1，是则ADD 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == 0:
            return {'result': True,
                    'describtion': 'Modify address Success',
            }

        else:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion': 'Modify address failed',
                    'errorimg': imgpath
            }

    def del_address(self, **w):

        driver = self.driver
        try:
            driver.find_element(*shoppingAddress).click()
            driver.switch_to_frame('iframe') #切进收货地址iframe

            #获取DEL前收货地址数量
            driver.switch_to_frame('iframe') #切进收货地址管理iframe
            addressnumbertext = driver.find_element(*addressNumber).text #获取‘已保存XX个地址’文字
            numberbefore = re.compile(r'\d{1}').search(addressnumbertext).group() #匹配出数字

            if numberbefore == 0 :
                imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
                driver.get_screenshot_as_file(imgpath)
                return {'result': False,
                        'describtion': 'No address to delete',
                        'errorimg': imgpath
                }

            driver.find_element(*deladdressLink).click()
            time.sleep(1)
            driver.switch_to_default_content() #恢复到默认状态
            driver.find_element(*okButton).click()


            #获取DEL后收货地址数量
            driver.switch_to_frame('iframe')
            driver.switch_to_frame('iframe')
            addressnumbertext = driver.find_element(*addressNumber).text
            numberchanged = re.compile(r'\d{1}').search(addressnumbertext).group()
            driver.switch_to_default_content() #恢复到默认状态

        except:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': sys.exc_info()[1],
                    'errorimg': imgpath
            }

        #判断DEL前后数字变化是否为-1，是则DEL 成功，否则失败
        if (int(numberchanged)-int(numberbefore)) == -1:
            return {'result': True,
                    'describtion': 'Delete address Success',
            }

        else:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result': False,
                    'describtion': 'Delete address failed',
                    'errorimg': imgpath
            }

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Chrome()
    d.maximize_window()
    testcase = dict(province='007041',city='007041001', country='007041001002', address='1234567', zipcode='123456',
                    name='sunyanhui', mobile='15135417896',telephone='0371-7127556',isdefault='yes' )
    d.get('http://www.company.com')
    print  slogin.Login(d).login('15000000372', '888888', '111')
    info = InfoCenter(d)
    #info.modify_password('888888', '888888', '888888')
    print info.del_address(**testcase)
    time.sleep(10)

    d.quit()
