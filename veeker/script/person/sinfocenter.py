#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from objectrepository.person.omycenter import *
from framework import setting
import time

class InfoCenter():


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

        except NoSuchElementException, e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }

        except e:
            imgpath = setting.ERRORIMGPATH+str(int(time.time()*100))+'.jpg'
            driver.get_screenshot_as_file(imgpath)
            return {'result':False,
                    'describtion':e,
                    'errorimg':imgpath
            }

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from selenium import webdriver
    import slogin
    d = webdriver.Ie()
    d.get('http://www.company.com')
    print  slogin.Login(d).login('15000000372', '888888', '111')
    info = InfoCenter(d)
    info.modify_password('888888', '888888', '888888')
    time.sleep(10)

    d.quit()
