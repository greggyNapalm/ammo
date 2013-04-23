# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import socket
import unittest

try:
    from http_parser.parser import HttpParser
except ImportError:
    from http_parser.pyparser import HttpParser

from ammo.phantom import HttpCompiler

TEST_SERV_ADDR = ('httpbin.org', 80)


class HTTPCompilerCase(unittest.TestCase):
    def test_eof(self):
        ''' Line endings satisfying RFC 2616.
        '''
        hc = HttpCompiler()
        headers = {
            'Host': 'httpbin.org',
            'Connection': 'close',
        }
        qs = '/path/to/some/resource'
        req = hc.build_raw(qs, method='GET', headers=headers)

        # Two lines at the end of request
        self.assertTrue(req.endswith('\r\n\r\n'))
        # Each line ends with <CR><LF>
        self.assertTrue(all([l.endswith('\r') for l in req.split('\n') if l]))

    def test_http_method(self):
        '''*method* kwarg effect.
        '''
        hc = HttpCompiler()
        headers = {
            'Host': 'httpbin.org',
            'Connection': 'close',
        }
        qs = '/path/to/some/resource'
        req = hc.build_raw(qs, method='GET', headers=headers)
        self.assertTrue(req.split('\r\n')[0].split(' ')[0] == 'GET')

    def test_constructor(self):
        ''' Instance attributes autosubstitution.
        '''
        headers = {
            'Host': 'httpbin.org',
            'Connection': 'close',
        }
        hc = HttpCompiler(method='PATCH', headers=headers)
        qs = '/path/to/check'
        req = hc.build_raw(qs)

        p = HttpParser()
        p.execute(req, len(req))
        result_hdrs = p.get_headers()

        self.assertTrue(p.get_method(), 'PATCH')
        self.assertTrue(all(
            [result_hdrs[h] == headers[h] for h in headers.keys()]))

    def test_phantom_format(self):
        ''' Request size calculation.
        '''
        headers = {
            'Host': 'httpbin.org',
            'Connection': 'close',
        }
        hc = HttpCompiler(method='PATCH', headers=headers)
        qs = '/path/to/check'
        req = hc.build_phantom(qs, body='Some stuff')
        p_len, p_req = req.split('\n', 1)

        self.assertTrue(int(p_len) == len(p_req))

    def test_httpbin_resp(self):
        '''Check HTTP status code of responce from real public server.
        '''
        hc = HttpCompiler()
        headers = {
            'Host': 'httpbin.org',
            'Connection': 'close',
        }
        qs = '/ip'
        req = hc.build_raw(qs, method='GET', headers=headers)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(TEST_SERV_ADDR)
        s.send(req)
        #s.send('GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n')
        resp = s.recv(100)  # 100 bytes enough for header.
        self.assertTrue('200 OK' in resp)
