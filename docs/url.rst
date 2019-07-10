.. _url:

Url
===

.. module:: http.url

Synopsis
--------

::

    >>> from http.url import Url
    >>> url = Url('http://pypi.python.org')
    >>> print url.netloc
    pypi.python.org
    >>> url.path.append('pypi')
    >>> print url.path
    /pypi
    >>> print url
    http://pypi.python.org/pypi

Interface
---------

:class:`Url` instances have the following methods:

.. autoclass:: Url()
   :members:
   :undoc-members:
