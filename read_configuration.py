# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 9:51 上午'
"""这个文件放入口函数"""

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def load_access_conf(conf="/Users/MRJ/PycharmProjects/qingcloud-test/access_key_qingyun.csv"):
    """
    读取配置文件
    :param file_name:
    :return:
    """

    assert conf.endswith(".csv"), "从官网下载的accessKey文件结尾应为csv"

    file = open(conf)
    config_dict = load(file, Loader=Loader)

    return config_dict


config_dict = load_access_conf()
qy_access_key_id = config_dict['qy_access_key_id']
qy_secret_access_key = config_dict['qy_secret_access_key']
base_url = 'https://api.qingcloud.com/iaas/?'
signature_method = 'HmacSHA1'
zone = 'sh1a'
