#!/usr/bin/python3.3 
# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException

class Base():

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True