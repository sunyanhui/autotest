#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 

import sys
import os
import unittest
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from action import slogin, sbrowser


class TestSomeThing(unittest.TestCase):
    def setUp(self):
        self.drive = sbrowser.Browser().open_browser()

    def tearDown(self):
        time.sleep(1)
        self.drive.quit()