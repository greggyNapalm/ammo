Ammo: Load testing input data generators
========================================

Installation
------------

Use pip and `vurtualev/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

::

    pip install -e git+git://github.com/greggyNapalm/ammo.git#egg=ammo

Example

::

    >>> from ammo.lunapark.generator import make_get_req
    >>> print make_get_req('/some-path/give-me-the-truth')
    155
    GET /some-path/give-me-the-truth HTTP/1.1
    Host: target.yandex.test
    User-Agent: TankKG v.default
    Referer: http://lunapark.yandex-team.ru
    Accept: */*
