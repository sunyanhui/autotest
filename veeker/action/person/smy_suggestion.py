#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from element.person.oplace_order import *
from common import output, common
import time

class MySuggestion():
    def __init__(self, driver):
        self.driver = driver


    def search(self):
        pass

    def valuation(self):
        pass

    def edit(self):
        pass

    def status(self):
        pass

    def detail(self):
        pass
