.. topic:: Easy-to-use and general-purpose HTTP library in Python

    ``http`` is a HTTP library for Python.

Basic Usage
===========

This module is heavily inspired by LWP and HTTP::Message.

::

    >>> from http import Request
    >>> req = Request('GET', 'http://google.com')
    >>> print req.method
    GET

User Guide
==========

.. toctree::
   :maxdepth: 2

   contents
