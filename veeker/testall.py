# coding=utf-8
from common import HTMLTestRunner
from common import config
from common import common
import unittest
import time, os

def create_test_unit(TEST_SUITE_DIR):
    u'''
    加载testsuite下所有的测试用例集
    '''
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(TEST_SUITE_DIR, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

if __name__ == '__main__':
    #获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    #定义个报告存放路径，支持相对路径
    filename = os.path.dirname(__file__) + "\\result\\result_%s.html"%now
    fp = open(filename,'wb')
    testunit = create_test_unit(".\\testsuite")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试报告')
    runner.run(testunit)
    fp.close()
    common.send_mail(filename, config.REPORT_RECEIVE_LIST)