# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import sys
import unittest
from unittest import mock

from mock import call

from cli import driver


class TestDriver(unittest.TestCase):

    def test_check_argument(self):
        args1 = ['1']
        dagp1 = mock.Mock(method='print_help', usage="")
        driver.argparse.ArgumentParser = dagp1
        driver.sys.exit = mock.Mock(return_value='exit -1')
        driver.check_argument(args1)
        calls = [call(prog='qingcloud ', usage='Please input service')]
        self.assertEqual(dagp1.call_args_list, calls)

        args2 = ['1', 'iaas']
        dagp2 = mock.Mock(method='print_help')
        driver.argparse.ArgumentParser = dagp2
        driver.sys.exit = mock.Mock(return_value='exit -1')
        driver.check_argument(args2)
        calls = [call(prog='qingcloud iaas', usage='Please input action [command <service> <action> [params]]')]
        self.assertEqual(dagp2.call_args_list, calls)

        args3 = ['1', 'iaas', '3']
        self.assertEqual(driver.check_argument(args3), None)

        # self.assertEqual(check_argument(args3), '-1')

    def test_get_action(self):
        amga = mock.Mock(return_value='issa')
        driver.ActionManager.get_action = amga
        self.assertEqual(driver.get_action('iaas','run-instance'), 'issa')
        self.assertEqual(driver.get_action('empty','run-instance'), 1001)

    def test_main(self):
        d_sys_argv = mock.MagicMock()
        driver.sys.argv = d_sys_argv
        check_argument = mock.Mock()
        driver.check_argument = check_argument
        get_action = mock.Mock()
        driver.get_action = get_action
        driver.main()
        self.assertEqual(check_argument.call_count,1)
        self.assertEqual(get_action.call_count,1)
