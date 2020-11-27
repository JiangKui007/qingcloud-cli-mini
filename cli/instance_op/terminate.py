# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:00 上午'
"""销毁实例"""
from cli.connection import explode_array
from .base import BaseAction


class TerminateInstancesAction(BaseAction):

    action = 'TerminateInstances'
    command = 'terminate-instances'
    usage = '%(prog)s -i "instance_id,..." ' \
            'See: https://docs.qingcloud.com/product/api/action/instance/terminate_instances.html'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                            action='store', type=str, default='',
                            help='the comma separated IDs of instances you want to terminate.')

        parser.add_argument('-d', '--direct_cease', dest='direct_cease',
                            action='store', type=str, default='',
                            help='the comma separated IDs of instances you want to terminate.')

        return parser

    @classmethod
    def build_directive(cls, options):
        required_params = {
            'zone': options.zone,
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None
        instances = explode_array(options.instances)
        if not instances:
            print('error: [instances] should be specified')
            return None

        return {'instances': instances,
                'direct_cease': options.direct_cease,
                'zone': options.zone
                }
