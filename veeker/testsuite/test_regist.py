#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 

import sys
import os
import unittest
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from script import slogin, sbrowser


class TestSomeThing(unittest.TestCase):
    def setUp(self):
        self.drive = sbrowser.Browser().openbrowser()

    def tearDown(self):
        time.sleep(1)
        self.drive.quit()