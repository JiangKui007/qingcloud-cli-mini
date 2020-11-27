# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
import mock

from cli.instance_op import describe, base
from cli.instance_op.describe import DescribeInstancesAction


class DescribeInstancesActionTest(unittest.TestCase):
    def test_add_ext_arguments(self):
        add_ext = mock.Mock(return_value='--mock')
        base.ArgumentParser.add_argument = add_ext
        parser = base.ArgumentParser
        DescribeInstancesAction.add_ext_arguments(parser)
        self.assertEqual(add_ext.call_count, 17)

    def test_build_directive(self):
        options = mock.Mock()
        describe.explode_array = mock.Mock()
        DescribeInstancesAction.build_directive(options)
        self.assertEqual(len(dir(options)), 37)

