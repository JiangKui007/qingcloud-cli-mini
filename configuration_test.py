# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '2020/11/23 10:03 上午'

import unittest
from unittest import mock

import configuration
# from read_configuration import load_access_conf


class TestConfigMethods(unittest.TestCase):

    def test_load_access_conf(self):
        rc_open = mock.MagicMock()
        configuration.open = rc_open
        rc_load = mock.MagicMock()
        configuration.load = rc_load
        access_dict = configuration.load_access_conf(conf="access_key_qingyun.csv")
        self.assertEqual(rc_open.call_count, 1)
        self.assertEqual(rc_load.call_count, 1)



if __name__ == '__main__':
    unittest.main()
