Ammo: Load testing input data generators
========================================

Installation
------------
Use pip and `vurtualev/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

from PyPI

::

    pip install ammo

from GitHub

::

    pip install -e git+git://github.com/greggyNapalm/ammo.git#egg=ammo

Example
-------

::

    >>> from ammo.phantom import HttpCompiler
    >>> HttpCompiler.version
    '3.1'
    >>> hc = HttpCompiler(method='GET', headers={'Host': 'httpbin.org'})
    >>> hc.build_phantom('/some/path')
    '73\nGET /some/path HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: httpbin.org\r\n\r\n\n'
    >>> 
    >>> hc.build_phantom('/other/path')
    '74\nGET /other/path HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: httpbin.org\r\n\r\n\n'
    >>> 
    >>> hc.build_phantom('/api/v1.0/resource', method='POST', body='{"a": "b"}',
    ...                  headers={'Host': 'httpbin.org', 'Content-type': 'application/json'})
    '148\nPOST /api/v1.0/resource HTTP/1.1\r\nAccept-Encoding: identity\r\nContent-Length: 10\r\nHost: httpbin.org\r\nContent-type: application/json\r\n\r\n{"a": "b"}\r\n\r\n\n'

Requirements
------------

* GNU Linux
* Python >= 2.7 (Not Python3)
