# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
from unittest import mock

from cli.instance_op import run, base
from cli.instance_op.run import RunInstancesAction


class RunInstancesActionTest(unittest.TestCase):

    def test_add_ext_arguments(self):  # add_argument参数调用了35次
        add_ext = mock.Mock(return_value='--mock')
        base.ArgumentParser.add_argument = add_ext
        parser = base.ArgumentParser
        RunInstancesAction.add_ext_arguments(parser)
        self.assertEqual(add_ext.call_count, 35)

    def test_build_directive(self):
        options = mock.Mock()
        run.explode_array = mock.Mock()
        run.RunInstancesAction.build_directive(options)
        self.assertEqual(len(dir(options)), 54)
