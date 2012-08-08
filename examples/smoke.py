#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ammo.examples
~~~~~~~~~~~~~

toss off examples.
"""

import io
import os
import sys
import httplib
import urllib

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
from ammo.phantom import HttpCompiler

def main():
    # basic
    query_strings = [
        '/api/v1/you',
        '/api/v1/can?run=false',
        '/api/v1/can?hide=true',
    ]

    sys.stdout.write('Minimalistic HTTP GET request\n')
    sys.stdout.write('-' * 80 + '\n')
    hc = HttpCompiler()
    for qs in query_strings:
        sys.stdout.write(hc.build_req(qs))

    # advanced
    sys.stdout.write('Slightly more complicated request\n')
    sys.stdout.write('-' * 80 + '\n')
    body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
    cntx_up = {
        'method':'PATCH',
        'Host':'custom.still-on-fire.ok',
        'kwargs': {
            'headers': {
                'Content-type': 'application/x-www-form-urlencoded',
                'Connection': 'close',
                'X-custom-header': 'some-value',
            },
            'body': urllib.urlencode(body)
        }
    }

    query_strings = []
    for id in range(3):
        params = urllib.urlencode({'where':'^right there', 'id':id})
        query_strings.append('%s?%s' % ('/some/path', params))

    hc = HttpCompiler(cntx_up=cntx_up)
    for qs in query_strings:
        sys.stdout.write(hc.build_req(qs))

if __name__ == '__main__':
        main()
