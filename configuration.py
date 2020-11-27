# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 9:51 上午'
"""这个文件放入口函数"""
from yaml import load, Loader

def load_access_conf(conf=""):
    """
    读取配置文件
    :param file_name:
    :return:
    """
    file = open(conf)
    return load(file, Loader=Loader)


# 传入绝对路径
config_dict = load_access_conf(conf="/Users/MRJ/PycharmProjects/qingcloud-cli-mini/access_key_qingyun.csv")
qy_access_key_id = config_dict['qy_access_key_id']
qy_secret_access_key = config_dict['qy_secret_access_key']
base_url = 'https://api.qingcloud.com/iaas/?'
signature_method = 'HmacSHA1'
zone = 'sh1a'
