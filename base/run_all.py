import unittest
from base import HTMLTestReportCN

# from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./")
print(suite.countTestCases())

f = open("report.html", 'wb')  # 二进制写格式打开要生成的报告文件
HTMLTestReportCN.HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
f.close()
