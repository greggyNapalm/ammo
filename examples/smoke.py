#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ammo.examples
~~~~~~~~~~~~~

toss off examples.
"""

import os
import sys
import urllib

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ammo.phantom import HttpCompiler


def main():
    # case #1: basic
    query_strings = [
        '/api/v1/you',
        '/api/v1/can?run=false',
        '/api/v1/can?hide=true',
    ]
    headers = {
        'Host': 'some.cool.org',
        'Connection': 'close'
    }
    sys.stdout.write('Minimalistic HTTP GET request\n')
    sys.stdout.write('-' * 80 + '\n')
    hc = HttpCompiler(method='GET', headers=headers)
    #hc = HttpCompiler()
    for qs in query_strings:
        sys.stdout.write(hc.build_phantom(qs))

    # case #2: advanced
    sys.stdout.write('Slightly more complicated request\n')
    sys.stdout.write('-' * 80 + '\n')
    body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
    headers = {
        'Host': 'some.cool.org',
        'Content-type': 'application/x-www-form-urlencoded',
        'X-custom-header': 'some-value',
        'Connection': 'close'
    }
    method = 'PATCH'
    body_encoded = urllib.urlencode(body)

    query_strings = []
    for id in range(3):
        params = urllib.urlencode({'where': '^right there', 'id': id})
        query_strings.append('%s?%s' % ('/some/path', params))

    hc = HttpCompiler(method=method, headers=headers)
    for qs in query_strings:
        sys.stdout.write(hc.build_phantom(qs, body=body_encoded))

    # case #3: advanced
    reqs = [
        (
            '/path/to/resource',
            {
                'method': 'GET',
                'headers': {
                    'Host': 'dom1.test.net',
                    'Connection': 'close'
                },
            }
        ),
        (
            '/just/one/more/resource',
            {
                'method': 'POST',
                'headers': {
                    'Host': 'dom2.test.net',
                    'Content-type': 'application/json'
                },
                'body': '{"a": "b"}',
            }
        ),
    ]
    hc = HttpCompiler()
    for r in reqs:
        sys.stdout.write(hc.build_phantom(r[0], **r[1]))

if __name__ == '__main__':
        main()
