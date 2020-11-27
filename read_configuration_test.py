# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:03 上午'

import unittest
from read_configuration import load_access_conf, base_url, signature_method


class TestConfigMethods(unittest.TestCase):

    def test_load_access_conf(self):
        access_dict = load_access_conf(conf="access_key_qingyun.csv")
        self.assertTrue(isinstance(access_dict, dict))

    def test_qy_access_key_id(self):
        access_dict = load_access_conf(conf="access_key_qingyun.csv")
        self.assertTrue(isinstance(access_dict['qy_access_key_id'], str))

    def test_qy_secret_access_key(self):
        access_dict = load_access_conf(conf="access_key_qingyun.csv")
        self.assertTrue(isinstance(access_dict['qy_secret_access_key'], str))

    def test_base_url(self):
        self.assertEqual(base_url, 'https://api.qingcloud.com/iaas/?')

    def test_signature_method(self):
        self.assertEqual(signature_method, 'HmacSHA1')

    def test_zone(self):
        self.assertEqual(signature_method, 'zone')


if __name__ == '__main__':
    unittest.main()
