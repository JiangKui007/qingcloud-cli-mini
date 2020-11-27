# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
from unittest import mock
import cli.instance_op

from cli.instance_op import ActionManager, describe


# def mock_action_table():
#     di = mock.Mock(return_value='describe-instances')
#     ti = mock.Mock(return_value='terminate-instances')
#     ri = mock.Mock(return_value='run-instances')
#     ActionManager.action_table = {
#         'run-instances': ri,
#         'terminate-instances': ti,
#         'describe-instances': di
#     }
#     return di, ti, ri, ActionManager.action_table
#

class TestActionManager(unittest.TestCase):
    def test_get_action(self):
        # di, ti, ri, action_table = mock_action_table()
        di = mock.Mock(return_value='describe-instances')
        ti = mock.Mock(return_value='terminate-instances')
        ri = mock.Mock(return_value='run-instances')
        ActionManager.action_table = {
            'run-instances': ri,
            'terminate-instances': ti,
            'describe-instances': di
        }
        self.assertEqual(ActionManager.get_action('describe-instances'), di)
        self.assertEqual(ActionManager.get_action('run-instances'), ri)
        self.assertEqual(ActionManager.get_action('terminate-instances'), ti)

    def test_get_valid_actions(self):
        di = mock.Mock(return_value='describe-instances')
        ti = mock.Mock(return_value='terminate-instances')
        ri = mock.Mock(return_value='run-instances')
        ActionManager.action_table = {
            'run-instances': ri,
            'terminate-instances': ti,
            'describe-instances': di
        }
        # di, ti, ri, ActionManager.action_table = mock_action_table()
        self.assertEqual(ActionManager.get_valid_actions(),
                         sorted(['describe-instances', 'run-instances', 'terminate-instances']))
