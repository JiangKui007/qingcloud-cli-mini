# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest

if __name__ == "__main__":
    # 测试用例保存的目录
    case_dirs = "/Users/MRJ/PycharmProjects/qingcloud-cli-mini"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_dirs, "*_test.py")
    # 运行测试用例同时保存测试报告
    test_report_path = "report.txt"
    with open(test_report_path, "a") as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(discover)
