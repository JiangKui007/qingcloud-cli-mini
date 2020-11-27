# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:00 上午'
"""获取实例"""
from cli.connection import explode_array
from .base import BaseAction


class DescribeInstancesAction(BaseAction):
    action = 'DescribeInstances'
    command = 'describe-instances'
    description = 'Param list see: https://docs.qingcloud.com/product/api/action/instance/terminate_instances.html'
    usage = '%(prog)s [-i "instance_id, ..."] [options]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                            action='store', type=str, default='',
                            help='一个或多个主机ID')

        parser.add_argument('-O', '--offset', dest='offset',
                            action='store', type=int, default=0,
                            help='数据偏移量, 默认为0')

        parser.add_argument('-L', '--limit', dest='limit',
                            action='store', type=int, default=20,
                            help='返回数据长度，默认为20，最大100')

        parser.add_argument('-T', '--tags', dest='tags',
                            action='store', type=str, default='',
                            help='一个或多个标签ID，按照标签ID过滤, 只返回已绑定某标签的资源')

        parser.add_argument('-s', '--status', dest='status',
                            action='store', type=str, default='',
                            help='一个或多个主机状态: pending, running, stopped, suspended, terminated, ceased')

        parser.add_argument('-m', '--image_id', dest='image_id',
                            action='store', type=str, default='',
                            help='一个或多个映像ID')

        parser.add_argument('-t', '--instance_type',
                            action='store', type=str,
                            dest='instance_type', default='',
                            help='一个或多个主机配置类型, 配置列表请参考'
                                 'https://docs.qingcloud.com/product/api/common/includes/instance_type.html#instance-type')

        parser.add_argument('-W', '--search_word', dest='search_word',
                            action='store', type=str, default='',
                            help='搜索关键词, 支持主机ID, 主机名称')

        parser.add_argument('-V', '--verbose', dest='verbose',
                            action='store', type=int, default=0,
                            help='是否返回冗长的信息, 若为1, 则返回主机相关其他资源的详细数据。')

        parser.add_argument('--instance_class', dest='instance_class',
                            action='store', type=int, default=0,
                            help='主机性能类型: 性能型:0, 超高性能型:1, 基础型:101, 企业型:201 ')

        parser.add_argument('--vcpus_current', dest='vcpus_current',
                            action='store', type=int, default=0,
                            help='主机CPU的核心数')

        parser.add_argument('--memory_current', dest='memory_current',
                            action='store', type=int, default=0,
                            help='主机内存大小')

        parser.add_argument('--os_disk_size', dest='os_disk_size',
                            action='store', type=int, default=0,
                            help='主机系统盘大小')

        parser.add_argument('--exclude_reserved', dest='exclude_reserved',
                            action='store', type=int, default=0,
                            help='是否过滤预留主机, 若为1, 则不返回预留主机信息')

        parser.add_argument('--dedicated_host_group_id', dest='dedicated_host_group_id',
                            action='store', type=int, default=0,
                            help='按照专属宿主机组过滤')

        parser.add_argument('--dedicated_host_id', dest='dedicated_host_id',
                            action='store', type=int, default=0,
                            help='按照专属宿主机组中某个宿主机过滤')

        parser.add_argument('--owner', dest='owner',
                            action='store', type=int, default=0,
                            help='按照用户账户过滤, 只返回指定账户的资源')

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
        return {
            'instances': explode_array(options.instances),
            'status': explode_array(options.status),
            'image_id': explode_array(options.image_id),
            'instance_type': explode_array(options.instance_type),
            'search_word': options.search_word,
            'verbose': options.verbose,
            'offset': options.offset,
            'limit': options.limit,
            'tags': explode_array(options.tags),
            'instance_class': options.instance_class,
            'vcpus_current': options.vcpus_current,
            'memory_current': options.memory_current,
            'os_disk_size': options.os_disk_size,
            'exclude_reserved': options.exclude_reserved,
            'dedicated_host_group_id': options.dedicated_host_group_id,
            'dedicated_host_id': options.dedicated_host_id,
            'owner': options.owner,
            'zone': options.zone
        }
