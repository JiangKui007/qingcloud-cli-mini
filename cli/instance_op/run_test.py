# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
import mock

from cli.instance_op import run, base
from cli.instance_op.run import RunInstancesAction


class RunInstancesActionTest(unittest.TestCase):

    def test_main(self):  # 成功调用success_send函数
        success_send = mock.Mock(return_value='200')
        base.send_request = success_send
        RunInstancesAction.main(['--image_id', 'bionic1x64c',
                                 '--zone', 'sh1a',
                                 '--login_mode', 'passwd',
                                 '--login_passwd', 'login_passwd',
                                 '-t', 's1.small.r1'])
        self.assertEqual(success_send.call_count, 1)

    def test_add_ext_arguments(self):  # add_argument参数调用了35次
        add_ext = mock.Mock(return_value='--mock')
        base.ArgumentParser.add_argument = add_ext
        parser = base.ArgumentParser
        RunInstancesAction.add_ext_arguments(parser)
        self.assertEqual(add_ext.call_count, 35)

    def test_get_argument_parser(self):
        parsed = RunInstancesAction.get_argument_parser().parse_args(
            ['--image_id', 'bionic1x64c',
             '--zone', 'sh1a',
             '--login_mode', 'passwd',
             '--login_passwd', 'login_passwd'])
        self.assertEqual(parsed.image_id, 'bionic1x64c')
        self.assertEqual(parsed.zone, 'sh1a')
        self.assertEqual(parsed.login_mode, 'passwd')
        self.assertEqual(parsed.login_passwd, 'login_passwd')

    def test_build_directive(self):
        options = mock.Mock()
        run.explode_array = mock.Mock()
        run.RunInstancesAction.build_directive(options)
        self.assertEqual(len(dir(options)), 54)
