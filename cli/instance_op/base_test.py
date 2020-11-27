# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import argparse
import unittest
import mock
import sys

from cli.instance_op import base
from read_configuration import load_access_conf
from argparse import ArgumentParser


class BaseActionTest(unittest.TestCase):

    def test_get_argument_parser(self):
        """

        :return:
        """
        ba = base.BaseAction
        add_common_arguments, add_ext_arguments = mock.Mock(), mock.Mock()
        ba.add_common_arguments = add_common_arguments
        ba.add_ext_arguments = add_ext_arguments
        self.assertTrue(type(ba.get_argument_parser()), type(ArgumentParser))
        self.assertEqual(add_common_arguments.call_count, 1)
        self.assertEqual(add_ext_arguments.call_count, 1)

    def test_add_common_arguments(self):
        """
        成功调用一次call_count
        :return:
        """
        ba = base.BaseAction
        add_ext = mock.Mock()
        base.ArgumentParser.add_argument = add_ext
        parser = ArgumentParser
        ba.add_common_arguments(parser)
        self.assertEqual(add_ext.call_count, 1)

    def test_main(self):
        """
        成功调用get_argument_parser，build_directive方法和send_request函数
        :return:
        """
        ba = base.BaseAction
        get_argument_parser, build_directive, success_send = mock.Mock(), mock.Mock(), mock.Mock()
        ba.get_argument_parser = get_argument_parser
        ba.build_directive = build_directive
        base.send_request = success_send
        ba.main([])
        self.assertEqual(get_argument_parser.call_count, 1)
        self.assertEqual(build_directive.call_count, 1)
        self.assertEqual(success_send.call_count, 1)

    def test_main_directive_none(self):
        """
        成功调用get_argument_parser，build_directive方法和send_request函数
        :return:
        """
        ba = base.BaseAction
        get_argument_parser, build_directive, success_send, sys_exit = mock.Mock(), mock.Mock(
            return_value=None), mock.Mock(), mock.Mock(return_value='-1')
        ba.get_argument_parser = get_argument_parser
        ba.build_directive = build_directive
        base.send_request = success_send
        sys.exit = sys_exit
        self.assertTrue(ba.main([]), sys.exit(-1))
        self.assertEqual(get_argument_parser.call_count, 1)
        self.assertEqual(build_directive.call_count, 1)
        self.assertEqual(success_send.call_count, 1)


if __name__ == '__main__':
    unittest.run()
