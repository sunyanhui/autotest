import unittest
import HTMLTestRunner
import sys

sys.path.append('\TestSuite')
from testsuite import *


testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(testlogin.TestLogin))

filename = 'd:/1.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='only a test', description='only a tset')
runner.run(testunit)