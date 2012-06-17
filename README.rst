Ammo: Load testing input data generators
========================================

Installation
------------

Use pip and `vurtualev/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

::

    pip install -e git+git://github.com/greggyNapalm/ammo.git#egg=ammo

Example
-------

::

    >>> import sys
    >>> from ammo.lunapark.generator import make_get_req
    >>> PATH = [
    ...     '/search/v2/coat?category=warm&text=big',
    ...     '/search/v2/coat?category=warm&text=supper',
    ...     '/search/v2/coat?category=warm&text=black',
    ... ]
    >>> for p in PATH:
    ...     sys.stdout.write(make_get_req(p))
    ...
    172
    GET /search/v2/coat?category=warm&text=big HTTP/1.1
    Host: target.changeme.com
    User-Agent: TankKG v.default
    Referer: https://github.com/greggyNapalm/ammo
    Accept: */*

    175
    GET /search/v2/coat?category=warm&text=supper HTTP/1.1
    Host: target.changeme.com
    User-Agent: TankKG v.default
    Referer: https://github.com/greggyNapalm/ammo
    Accept: */*

    174
    GET /search/v2/coat?category=warm&text=black HTTP/1.1
    Host: target.changeme.com
    User-Agent: TankKG v.default
    Referer: https://github.com/greggyNapalm/ammo
    Accept: */*

    >>> sys.stdout.write('0\n')
    0
