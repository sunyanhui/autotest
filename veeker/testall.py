# coding=utf-8
import unittest
import HTMLTestRunner
import sys, time
from framework import setting, common_method

def create_test_unit():
    u'''
    加载testsuite下所有的测试用例集
    '''
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(setting.TESTSUITEDIR, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

def crete_test_single():
    u'''
    加载单个模块用例，暂时不用
    '''
    testunit = unittest.TestSuite()

if __name__ == '__main__':

    filename = setting.REPORTDIR + str(int(time.time() * 100)) + '.html'
    fp = open(filename,'wb')
    testunit = create_test_unit()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='only a test', description='only a tset')
    runner.run(testunit)
    common_method.sendmail(filename, setting.REPORTTOLIST)