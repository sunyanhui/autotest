# coding=utf-8
import unittest
import HTMLTestRunner
import time
from common import config, common_method

def create_test_unit():
    u'''
    加载testsuite下所有的测试用例集
    '''
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(config.TESTSUITEDIR, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

if __name__ == '__main__':

    #获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    #定义个报告存放路径，支持相对路径
    filename = ".\\result\\result_%s.html"%now
    fp = open(filename,'wb')
    testunit = create_test_unit()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试报告')
    runner.run(testunit)
    common_method.sendmail(filename, config.REPORTTOLIST)