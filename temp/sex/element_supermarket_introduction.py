#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

introduction_link = (By.LINK_TEXT, u'超市简介')

introduction = (By.ID, 'two1')

culture = (By.ID, 'two2')

structure = (By.ID, 'two3')

introduction_rich_text = 'enterIntroClob'

culture_rich_text = 'enterCultureClob'

structure_rich_text = 'structureIdClob'

introduction_button = (By.XPATH, "//div[@id='con_two_1']/div[2]/input")

culture_button = (By.XPATH, "//div[@id='con_two_2']/div[2]/input")

structure_button = (By.XPATH, "//div[@id='con_two_3']/div[2]/input")

confirm = (By.ID, 'popup_ok')