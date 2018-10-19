#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import HTMLTestReportCN.HTMLTestReportCN

suite = unittest.TestSuite()  # 创建测试套件
all_cases = unittest.defaultTestLoader.discover('./testCase/', 'test_*.py')
# 找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来

fp = file('./result/test_report.html', 'wb')
runner = HTMLTestReportCN.HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title='钱街测试报告',
            description='This demonstrates the report output by HTMLTestRunner.'
            )
runner.run(suite)