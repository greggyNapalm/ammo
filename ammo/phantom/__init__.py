#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ammo.phantom
~~~~~~~~~~~~

Functions to generate raw HTTP request.
"""

import pprint
pp = pprint.PrettyPrinter(indent=4)
import io
import httplib


class HttpCompiler(object):
    version = '2.0'

    def __init__(self, method=None, headers=None):
        self.method = method
        self.headers = headers

    def build_raw(self, url, method=None, body=None, headers=None, tag=None):
        '''
        @see http://docs.python.org/2.7/library/httplib.html#httplib.HTTPConnection.request
        '''
        headers = headers or self.headers
        assert isinstance(headers, dict)
        host = headers.get('Host', None)
        assert host
        method = method or self.method
        assert method

        conn = httplib.HTTPConnection(host)
        bio = io.BytesIO()
        bio.sendall = bio.write
        conn.sock = bio
        conn.request(method, url, body=body, headers=headers)
        return bio.getvalue().decode('utf-8')

    def build_phantom(self, *args, **kwargs):
        req = self.build_raw(*args, **kwargs)
        tag = kwargs.get('tag', None)
        if tag:
            return '{} {}\n{}'.format(len(req), tag, req)
        return '{}\n{}'.format(len(req), req)
