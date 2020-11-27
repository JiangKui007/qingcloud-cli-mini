# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
from unittest import mock

from cli.instance_op import terminate, base
from cli.instance_op.terminate import TerminateInstancesAction


class TerminateInstancesActionTest(unittest.TestCase):
    def test_add_ext_arguments(self):
        add_ext = mock.Mock(return_value='--mock')
        base.ArgumentParser.add_argument = add_ext
        parser = base.ArgumentParser
        TerminateInstancesAction.add_ext_arguments(parser)
        self.assertEqual(add_ext.call_count, 2)

    def test_build_directive(self):
        options = mock.Mock()
        terminate.explode_array = mock.Mock()
        TerminateInstancesAction.build_directive(options)
        self.assertEqual(len(dir(options)), 22)

