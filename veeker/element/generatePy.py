#coding=utf-8
import xlrd
import os

#定位方式翻译字典
locationDict = {
    'id':'By.ID',
    'link':'By.LINK_TEXT',
    'name':'By.NAME',
    'class':'By.CLASS_NAME',
    'css':'By.CSS_SELECTOR',
    'xpath':'By.XPATH',
    'partial_link':'By.PARTIAL_LINK_TEXT'}

def creat_element_file(excel, excel_name, tableName):
    u'''
    生成元素文档
    '''
    #根据表名获取表对象
    table = excel.sheet_by_name(tableName)

    #获取总行数
    lineNum = table.nrows

    if lineNum == 0:return

    #类名
    objectName = 'Element' + ''.join([i.capitalize() for i in tableName.split("_")] )

    #模块名
    moduleName = 'element_' + excel_name + '_' + tableName.lower() + '.py'

    #文档内容
    S = '''#!/usr/bin/python2.7\n# -*- coding: utf-8 -*-\nfrom selenium.webdriver.common.by import By\n\nclass %s(object):\n\n'''%(objectName)

    #循环追加定位元素，如：把EXCEL里的account  id  idInput 转换成    account = (By.ID,u"idInput")
    for i in range(1,lineNum):
        line = table.row_values(i)
        S = S + '''    #%s\n    %s = (%s,u"%s")\n\n'''%(line[3], line[0], locationDict[line[1]], line[2])

    with open(moduleName, 'w') as module:
        module.write(S.encode('utf-8'))

if __name__ == '__main__':
    file_list = [x for x in os.listdir('.') if x.endswith('.xls')]
    for xls in file_list:
        excel = xlrd.open_workbook(xls)
        excel_name = xls.split('.')[0]
        sheetNames = excel.sheet_names()

        for i in sheetNames:
            if i == u"目录":
                continue
            creat_element_file(excel, excel_name, i)