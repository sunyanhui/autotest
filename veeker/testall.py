import unittest
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append('\TestSuite')
sys.path.append('\TestSuite\person')
from testsuite.person import testorder


testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(testorder.TestOrder))

filename = 'd:/1.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='only a test', description='only a tset')
runner.run(testunit)