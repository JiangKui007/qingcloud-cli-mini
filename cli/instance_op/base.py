# =========================================================================
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

# _*_ coding:utf-8 _*_
# __author__ = 'Edison'
import sys
from argparse import ArgumentParser
from cli.connection import send_request

class BaseAction(object):

    action = ''
    command = ''
    usage = ''
    description = ''

    @classmethod
    def get_argument_parser(cls):
        parser = ArgumentParser(
            prog='qingcloud iaas %s' % cls.command,
            usage=cls.usage,
            description=cls.description
        )

        cls.add_common_arguments(parser)
        cls.add_ext_arguments(parser)
        return parser

    @classmethod
    def add_common_arguments(cls, parser):
        parser.add_argument('-z', '--zone', dest='zone',
                            action='store', type=str, default=None,
                            help='the ID of zone you want to access.'
                                 ' Will change configuration settings if you specific.')

    @classmethod
    def main(cls, args):
        parser = cls.get_argument_parser()
        options = parser.parse_args(args)
        directive = cls.build_directive(options)
        if directive is None:
            parser.print_help()
            sys.exit(-1)
        return send_request(cls.action, directive)
