# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:00 上午'
from cli.instance_op import run
from cli.instance_op import describe
from cli.instance_op import terminate


class ActionManager(object):

    @classmethod
    def get_action(cls, action):
        return cls.action_table.get(action)

    @classmethod
    def get_valid_actions(cls):
        return sorted(ActionManager.action_table.keys())

    action_table = {'describe-instances': describe.DescribeInstancesAction,
                    'terminate-instances': terminate.TerminateInstancesAction,
                    'run-instances': run.RunInstancesAction}

