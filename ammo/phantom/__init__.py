#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ammo.phantom
~~~~~~~~~~~~

Functions to generate raw HTTP request.
"""

import io
#import sys
import httplib
#import urllib


class HttpCompiler(object):
    version = '1.0'

    def __init__(self, cntx_up=None):
        self.method = None
        self.qs = None
        self.headers = {}
        self.defaults = {
            'method': 'GET',
            'Host': 'target.on-fire.io',
            'kwargs': {},
            #'body': '{body}',
        }
        self.cntx = self.defaults
        if cntx_up:
            self.cntx.update(cntx_up)

        conn = httplib.HTTPConnection(self.cntx['Host'])
        bio = io.BytesIO()
        bio.sendall = bio.write
        conn.sock = bio
        conn.request(self.cntx['method'], '{qs}', **self.cntx['kwargs'])
        self.tmpl = bio.getvalue().decode('utf-8')

    def build_req(self, qs, body):
        return self.tmpl % qs

    def from_dict(self, **kwargs):
        host = kwargs.get('Host', None) or self.headers['Host']
        method = kwargs.get('method', None) or self.method
        qs = kwargs.get('qs', None) or self.qs
        kw = {
            'headers': kwargs.get('headers', None) or self.headers,
            'body': kwargs.get('body', None) or self.body,
        }

        conn = httplib.HTTPConnection(host)
        bio = io.BytesIO()
        bio.sendall = bio.write
        conn.sock = bio
        conn.request(method, qs, **kw)
        return bio.getvalue().decode('utf-8')
