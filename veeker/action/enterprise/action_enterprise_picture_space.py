#!/usr/bin/python2.7
#coding=utf-8

import time
from element.element_enterprise_picture_space import ElementPictureSpace
from action.basepage import BasePage
from common import output
from common.config import IMGPATH
import os
from selenium.webdriver.common.by import By



class EnterprisePictureSpace(BasePage, ElementPictureSpace):
    u'''
    企业图片空间
    '''

    def add_picture(self, imgpath=os.path.join(IMGPATH, 'meinv.jpg'), *args, **kwargs):
        u'''
        上传图片
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.picture_space_link).click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(3)
            find_element(self.upload_link).click()
            driver.switch_to_frame("totalIframe")
            find_element(self.add_picture_button).click()
            time.sleep(1)
            if not self.upload_photo(imgpath):
                return output.error_user_defined(driver, '添加图片失败')
            time.sleep(1)
            find_element(self.upload_button).click()
            time.sleep(2)
        except:
            return output.error_user_defined(driver, "上传图片失败")
        else:
            return output.pass_user_defined(driver, "上传图片成功" )
        finally:
            driver.switch_to_default_content()
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

    def del_picture(self, img_name='meinv.jpg', *args, **kwargs):
        u'''
        上传图片
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.picture_space_link).click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(3)
            driver.switch_to_frame("totalIframe")
            find_element((By.XPATH, self.del_link[1]%img_name)).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
            find_element(self.confirm).click()
        except:
            return output.error_user_defined(driver, "删除图片失败")
        else:
            return output.pass_user_defined(driver, "删除图片成功" )
        finally:
            driver.switch_to_default_content()
            driver.close()
            driver.switch_to_window(driver.window_handles[0])



    def empty(self, *args, **kwargs):
        u'''
        清空回收站
        '''

        driver = self.driver
        find_element = self.find_element
        select = self.select

        try:
            find_element(self.picture_space_link).click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(3)
            find_element(self.recycle_link).click()
            driver.switch_to_frame("totalIframe")
            find_element(self.empty_link).click()
            driver.switch_to_default_content()
            find_element(self.confirm).click()
        except:
            return output.error_user_defined(driver, "清空回收站失败")
        else:
            return output.pass_user_defined(driver, "清空回收站成功" )
        finally:
            driver.switch_to_default_content()
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

if __name__ =='__main__':
    from action.action_login import Login
    a = Login()
    a.open_browser("http://www.wiki100.cn")
    a.login(username = 'XYHD3100028',password = '888888')

    b = EnterprisePictureSpace()
    error = b.add_picture()
    b.del_picture()
    b.empty()