# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import sys
import hmac
import base64
import datetime
from hashlib import sha1, sha256

import urllib.parse as urllib

import requests
import json
from read_configuration import config_dict, signature_method, base_url, zone


def explode_array(list_str, separator=","):
    """
    Explode list string into array
    """
    if not list_str:
        return []
    return [item.strip() for item in list_str.split(separator) if item.strip() != '']


def send_request(action, directive):
    parmas = {
        'signature_version': 1,
        'signature_method': signature_method,
        'version': 1,
        'access_key_id': config_dict['qy_access_key_id'],
        'action': action,
        'time_stamp': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        #'zone': zone,
    }

    for k, v in directive.items():
        if v:
            if isinstance(v, list):
                for i in range(1, len(v) + 1):
                    parmas[k + '.' + str(i)] = v[i - 1]
            else:
                parmas[k] = v

    url_parmas = url_convert(parmas=parmas)
    url = signature(url_parmas=url_parmas)
    # TODO: delete
    print(url)
    load_response(url)


def load_response(url):
    res = requests.get(url)
    if res.status_code == 200:
        js_res = json.loads(res.content)
        print(json.dumps(js_res, indent=4, sort_keys=True))
    else:
        print('bad request')


def signature(method='GET', uri='/iaas/', url_parmas=''):
    """
    https://docs.qingcloud.com/api/common/signature.html
    """
    string_to_sign = method + '\n' + uri + '\n' + url_parmas
    h = hmac.new(config_dict['qy_secret_access_key'].encode(), digestmod=sha1)
    h.update(string_to_sign.encode())
    sign = base64.b64encode(h.digest())
    signature = urllib.quote_plus(sign)
    return base_url + url_parmas + '&signature=' + signature


def url_convert(parmas=[]):
    for k, v in parmas.items():
        if not isinstance(v, int):
            parmas[k] = urllib.quote_plus(v)
    sorted_parmas = sorted(parmas.items(), key=lambda d: d[0])

    url_parmas = ''
    for k, v in sorted_parmas:
        url_parmas = url_parmas + '&' + k + '=' + str(v)
    return url_parmas[1:]


if __name__ == '__main__':
    print(signature())
