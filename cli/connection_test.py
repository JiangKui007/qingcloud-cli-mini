# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import unittest
import io
import urllib

from unittest import mock
import sys

from cli import connection
from cli.connection import explode_array, send_request, signature, url_convert, load_response

#
# def stub_stdin(testcase_inst, inputs):
#     stdin = sys.stdin
#
#     def cleanup():
#         sys.stdin = stdin
#
#     testcase_inst.addCleanup(cleanup)
#     sys.stdin = io.StringIO(inputs)


def stub_stdout(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()

# This method will be used by the mock to replace requests.get

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.content = json_data
            self.status_code = status_code

    if args[0] == 'pass':
        return MockResponse('{"key1": "value1"}', 200)
    elif args[0] == 'refuse':
        return MockResponse('{"key2": "value2"}', 201)

    return MockResponse(None, 404)


class TestConnection(unittest.TestCase):
    def test_explode_array(self):
        m1_list_str = '1,2,3,4'
        m2_list_str = '2 ,3,  4 ,  5,  8'
        separator = ','
        self.assertEqual(explode_array(m1_list_str, separator), ['1', '2', '3', '4'])
        self.assertEqual(explode_array(m2_list_str, separator), ['2', '3', '4', '5', '8'])

    def test_send_request(self):
        action = ""
        directive = mock.MagicMock(dict)
        url_convert = mock.Mock()
        connection.url_convert = url_convert
        signature = mock.Mock()
        connection.signature = signature
        load_response = mock.Mock()
        connection.load_response = load_response

        send_request(action, directive)

        self.assertTrue(url_convert.called)
        self.assertTrue(signature.called)
        self.assertTrue(load_response.called)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_load_response_pass(self, get_mock):
        json_dumps = mock.Mock()
        connection.json.dumps = json_dumps
        load_response('pass')
        self.assertTrue(json_dumps.called)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_load_response_refuse(self, get_mock1):
        json_dumps = mock.Mock()
        connection.json.dumps = json_dumps
        stub_stdout(self)
        load_response('refuse')
        self.assertFalse(json_dumps.called)
        self.assertEqual(str(sys.stdout.getvalue()), 'bad request\n')


    def test_signature(self):
        url_parmas = 'zone=sh1a'
        quote_plus = mock.Mock(return_value='signatured_value')
        connection.urllib.quote_plus = quote_plus
        signatured_url = signature(url_parmas=url_parmas)
        self.assertTrue(signatured_url.startswith('https://api.qingcloud.com/iaas/?'))
        self.assertTrue(signatured_url.endswith('&signature=signatured_value'))
        self.assertTrue('zone=sh1a' in signatured_url)
        self.assertTrue(quote_plus.called)


    def test_url_convert(self):
        parmas = {'k1':'v1','k3':'v3','k4':'v4','k2':'v2'}
        quote_plus_uc = mock.Mock(return_value='signatured_value_uc')
        connection.urllib.quote_plus = quote_plus_uc
        self.assertEqual(url_convert(parmas),'k1=signatured_value_uc&k2=signatured_value_uc&k3=signatured_value_uc&k4=signatured_value_uc')
