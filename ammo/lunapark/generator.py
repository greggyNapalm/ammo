#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ammo.lunapark.generators
~~~~~~~~~~~~~~~~~~

This module provides helper functions for Lunapark ammo creation
"""

import sys
import urllib

# constraints
EOL = '\r\n'

# multi_part params
in_file = '/path/to/some/big/file'
content_type = 'multipart/form-data'
boundary = '------------------------------d7c3d7c4089e'
body_part = 'Content-Disposition: form-data; name="request"; filename="nm.xml"'
body_type = 'Content-Type: application/xml'


def make_post_req(req_path, body, context_up=None):
    ''' Create POST HTTP requset, calc size of it.
    Args:
        req_path: str - request path
        body: str - request body
        context_up: dict - update some request attributes if needed

    Returns:
        str - HTTP request in plain-text with size in bytes'''

    context = {
            'protocol': 'HTTP/1.1',
            'Host': 'target.changeme.test',
            'User-Agent': 'TankKG v.default',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://github.com/greggyNapalm/ammo',
            'Accept': '*/*',
            'Cookies': [],
        }

    if context_up:
        context.update(context_up)

    if 'session_id' in context:
        context['Cookies'].append('Session_id=' + context['session_id'])

    req = 'POST ' + req_path + ' ' + context['protocol'] + EOL
    req += 'Host: ' + context['Host'] + EOL
    req += 'User-Agent: ' + context['User-Agent'] + EOL
    req += 'Content-Type: ' + context['Content-Type'] + EOL
    req += 'Referer: ' + context['Referer'] + EOL
    req += 'Accept: ' + context['Accept'] + EOL
    req += 'Content-Length: ' + str(len(body)) + EOL
    req += EOL + body + EOL
    req += EOL
    return str(len(req)) + '\n' + req,


def make_multi_part(req_path, body):
    ''' Create multipart POST HTTP requset.
    Args:
        req_path: str - request path
        body: str - request body

    Returns:
        str - HTTP request in plain-text with size in bytes'''

    d_host = 'target.changeme.test'
    d_usr_agent = 'TankKG v.default'

    fmt_body = '--' + boundary + EOL
    fmt_body += body_part + EOL
    fmt_body += body_type + EOL + EOL
    fmt_body += body + EOL + EOL
    fmt_body += '--' + boundary + '--'

    req = 'POST ' + req_path + ' HTTP/1.1' + EOL
    req += 'Host: ' + d_host + EOL
    req += 'User-Agent: ' + d_usr_agent + EOL
    req += 'Accept: */*' + EOL
    req += 'Expect: 100-continue' + EOL
    req += 'Content-Type: multipart/form-data; boundary=' + boundary + EOL
    req += 'Content-Length: ' + str(len(fmt_body)) + EOL
    req += EOL + fmt_body + EOL + EOL
    return str(len(req)) + "\n" + req


def make_get_req(req_path, context_up=None):
    ''' Create GET HTTP requset, calc size of it.
    Args:
        req_path: str - request path
        context_up: dict - update some request attributes if needed

    Returns:
        str - HTTP request in plain-text with size in bytes'''

    context = {
            'protocol': 'HTTP/1.1',
            'Host': 'target.changeme.com',
            'User-Agent': 'TankKG v.default',
            'Referer': 'https://github.com/greggyNapalm/ammo',
            'Accept': '*/*',
            'Cookies': [],
        }

    if context_up:
        context.update(context_up)

    req = 'GET ' + req_path + ' ' + context['protocol'] + EOL
    req += 'Host: ' + context['Host'] + EOL
    req += 'User-Agent: ' + context['User-Agent'] + EOL
    req += 'Referer: ' + context['Referer'] + EOL
    req += 'Accept: ' + context['Accept'] + EOL

    if 'session_id' in context:
        context['Cookies'].append('Session_id=' + context['session_id'])

    if 'Connection' in context:
        req += 'Connection: ' + context['Connection'] + EOL

    req += EOL
    return str(len(req)) + '\n' + req

if __name__ == '__main__':
    try:
        body_file = open(in_file, "r")
        f_body = body_file.read()
        body_file.close()
    except IOError, e:
        print 'Cant\'t read ', in_file, '\n', e
        sys.exit(1)
    pass
    make_multi_part('/chnageme/api/', f_body)
    print '0',
