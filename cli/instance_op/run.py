# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:00 上午'
"""创建实例"""

from cli.connection import explode_array
from .base import BaseAction

class RunInstancesAction(BaseAction):

    action = 'RunInstances'
    command = 'run-instances'
    description = 'Param list see: https://docs.qingcloud.com/product/api/action/instance/run_instances.html'
    usage = '%(prog)s --image_id <image_id> --instance_type <instance_type>'
    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-m', '--image_id', required=True, dest='image_id',
                            action='store', type=str, default='',
                            help='image ID,'
                                 '此映像将作为主机的模板。可传青云提供的映像ID，或自己创建的映像ID')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                            action='store', type=str, default=None,
                            help='instance type: '
                                '如果使用物理主机, 该参数必填。'
                                '如果请求中指定了 instance_type，cpu 和 memory 参数可略过。'
                                '如果请求中没有 instance_type，则 cpu 和 memory 参数必须指定。'
                                '如果请求参数中既有 instance_type，又有 cpu 和 memory，则以 cpu, memory 的值为准。'
                                'See available instance-type at：\
                                https://docs.qingcloud.com/product/api/common/includes/instance_type.html#instance-type')

        parser.add_argument('-c', '--count', dest='count',
                            action='store', type=int, default=1,
                            help='the number of instances to launch, default 1.')

        parser.add_argument('-C', '--cpu', dest='cpu',
                            action='store', type=int, default=None,
                            help='cpu core: 1, 2, 4, 8, 16')

        parser.add_argument('-M', '--memory', dest='memory',
                            action='store', type=int, default=None,
                            help='memory size in MB: 1024, 2048, 4096, 6144, 8192, 12288, 16384, 24576, 32768')

        parser.add_argument('-N', '--instance_name', dest='instance_name',
                            action='store', type=str, default='',
                            help='instance name')

        parser.add_argument('-n', '--vxnets', dest='vxnets',
                            action='store', type=str, default=None,
                            help='specifies the IDs of vxnets the instance will join.')

        parser.add_argument('-s', '--security_group', dest='security_group',
                            action='store', type=str, default=None,
                            help='the ID of security group that will be applied to instance')

        parser.add_argument('-l', '--login_mode', required=True, dest='login_mode',
                            action='store', type=str, default=None,
                            help='SSH login mode: keypair or passwd')

        parser.add_argument('-p', '--login_passwd', dest='login_passwd',
                            action='store', type=str, default='',
                            help='login_passwd, should specified when SSH login mode is "passwd".')

        parser.add_argument('-k', '--login_keypair', dest='login_keypair',
                            action='store', type=str, default='',
                            help='login_keypair, should specified when SSH login mode is "keypair".')

        parser.add_argument('-o', '--os_disk_size', dest='os_disk_size',
                            action='store', type=str, default='',
                            help='System disk size, Linux available values :20-100, default:20. '
                                 ' Windows available values: 50-100, default:50.')

        parser.add_argument('--volumes', dest='volumes',
                            action='store', type=str, default='',
                            help='主机创建后自动加载的硬盘ID，如果传此参数，则参数 count 必须为1 .')

        parser.add_argument('--hostname', dest='hostname',
                            action='store', type=str, default='',
                            help='可指定主机的 hostname')

        parser.add_argument('--need_newsid', dest='need_newsid',
                            action='store', type=str, default=0,
                            help='1: 生成新的SID，0: 不生成新的SID, 默认为0；只对Windows类型主机有效。.')

        parser.add_argument('--instance_class', dest='instance_class',
                            action='store', type=str, default='',
                            help='主机性能类型: 性能型:0, 超高性能型:1, 基础型:101, 企业型:201')

        parser.add_argument('--cpu_model', dest='cpu_model',
                            action='store', type=str, default='',
                            help='CPU 指令集, 有效值: Westmere, SandyBridge, IvyBridge, Haswell, Broadwell.')

        parser.add_argument('--cpu_topology', dest='cpu_topology',
                            action='store', type=str, default='',
                            help='CPU 拓扑结构: 插槽数, 核心数, 线程数; 插槽数 * 核心数 * 线程数 应等于您应选择的CPU数量。.')

        parser.add_argument('--gpu', dest='gpu',
                            action='store', type=str, default='',
                            help='GPU 个数.')

        parser.add_argument('--gpu_class', dest='gpu_class',
                            action='store', type=str, default='',
                            help='GPU 类型，有效值有 0 和 1 。0 对应的是 NVIDIA P100，1 对应的是 AMD S7150.')

        parser.add_argument('--nic_mqueue', dest='nic_mqueue',
                            action='store', type=str, default='',
                            help='网卡多对列: 关闭(默认)：0，开启：1.')

        parser.add_argument('--need_userdata', dest='need_userdata',
                            action='store', type=str, default='',
                            help='1: 使用 User Data 功能；0: 不使用 User Data 功能；默认为 0 。.')

        parser.add_argument('--userdata_type', dest='userdata_type',
                            action='store', type=str, default='',
                            help='User Data 类型，有效值：’plain’, ‘exec’ 或 ‘tar’。为 ‘plain’或’exec’ 时，'
                                 '使用一个 Base64 编码后的字符串；为 ‘tar’ 时，使用一个压缩包（种类为 zip，tar，tgz，tbz）。.')

        parser.add_argument('--userdata_value', dest='userdata_value',
                            action='store', type=str, default='',
                            help='User Data 值。当类型为 ‘plain’ 时，为字符串的 Base64 编码值，长度限制 4K；当类型为 ‘tar’，'
                                 '为调用UploadUserDataAttachment返回的 attachment_id。.')

        parser.add_argument('--userdata_path', dest='userdata_path',
                            action='store', type=str, default='',
                            help='User Data 和 MetaData 生成文件的存放路径。'
                                 '不输入或输入不合法时，为默认目录 /etc/qingcloud/userdata.')

        parser.add_argument('--userdata_file', dest='userdata_file',
                            action='store', type=str, default='',
                            help='userdata_type 为 ‘exec’ 时，指定生成可执行文件的路径，默认为/etc/rc.local.')

        parser.add_argument('--target_user', dest='target_user',
                            action='store', type=str, default='',
                            help='目标用户 ID ，可用于主账号为其子账号创建资源。.')

        parser.add_argument('--dedicated_host_group_id', dest='dedicated_host_group_id',
                            action='store', type=str, default='',
                            help='虚机创建到指定的专属宿主机组中.')

        parser.add_argument('--dedicated_host_id', dest='dedicated_host_id',
                            action='store', type=str, default='',
                            help='虚机创建到某专属宿主机组中指定的宿主机上.')

        parser.add_argument('--instance_group', dest='instance_group',
                            action='store', type=str, default='',
                            help='虚机创建加入到指定的主机组中.')

        parser.add_argument('--hypervisor', dest='hypervisor',
                            action='store', type=str, default='',
                            help='hypervisor 类型，当前支持 kvm 和 bm, 默认是 kvm.')

        parser.add_argument('--os_disk_encryption', dest='os_disk_encryption',
                            action='store', type=str, default='',
                            help='创建加密主机.')

        parser.add_argument('--cipher_alg', dest='cipher_alg',
                            action='store', type=str, default='',
                            help='加密使用的算法类型:.目前仅支持 aes256，默认 aes256')

        parser.add_argument('--months', dest='months',
                            action='store', type=str, default='',
                            help='如果购买合约模式的主机，需要传此参数，数值为购买的月份数。.')

        parser.add_argument('--auto_renew', dest='auto_renew',
                            action='store', type=str, default='',
                            help='如果购买合约模式的主机，可传此参数，数值为合约到期后自动续约的月份数。'
                                 '如果购买合约时不传此参数，合约到期则不会自动续约。')

        return parser

    @classmethod
    def build_directive(cls, options):

        required_params = {
            'image_id': options.image_id,
            'zone': options.zone,
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        if not options.instance_type:
            if not options.cpu or not options.memory:
                print(
                    'error: [instance_type] should be specified or specify both [cpu] and [memory]')
                return None

        if options.volumes:
            if not options.count or (options.count == 1):
                print(
                    'error: [count] should be set 1 when [volumes] is specified')
                return None

        return {
            'image_id': options.image_id,
            'instance_type': options.instance_type,
            'cpu': options.cpu,
            'memory': options.memory,
            'instance_name': options.instance_name,
            'count': options.count,
            'vxnets': explode_array(options.vxnets),
            'security_group': options.security_group,
            'login_mode': options.login_mode,
            'login_passwd': options.login_passwd,
            'login_keypair': options.login_keypair,
            'volumes': options.volumes,
            'hostname': options.hostname,
            'need_newsid': options.need_newsid,
            'instance_class': options.instance_class,
            'cpu_model': options.cpu_model,
            'cpu_topology': options.cpu_topology,
            'gpu': options.gpu,
            'gpu_class': options.gpu_class,
            'nic_mqueue': options.nic_mqueue,
            'need_userdata': options.need_userdata,
            'userdata_type': options.userdata_type,
            'userdata_value': options.userdata_value,
            'userdata_path': options.userdata_path,
            'userdata_file': options.userdata_file,
            'target_user': options.target_user,
            'dedicated_host_group_id': options.dedicated_host_group_id,
            'dedicated_host_id': options.dedicated_host_id,
            'instance_group': options.instance_group,
            'hypervisor': options.hypervisor,
            'os_disk_encryption': options.os_disk_encryption,
            'cipher_alg': options.cipher_alg,
            'months': options.months,
            'auto_renew': options.auto_renew,
            'zone': options.zone
        }
