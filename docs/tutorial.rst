.. _getting_started:

Getting started: How to use http
================================

The goal of this documentation is to provide you with all the information required to effectively use the ``http`` library.

Core
----

http is heavily inspired by LWP and HTTP::Message. It provides the following classes:

#. Request
#. Response
#. Headers
#. Date
#. Url
#. HTTPException

Request
-------

    >>> from http import Request
    >>> request = Request('GET', 'http://lumberjaph.net')
    

``Request`` is a class encapsulating HTTP style request, consisting of a request line, some headers, and a content body.

The HTTP method can be anything, and is case-sensitive: *get* is different from *GET*.

Headers
~~~~~~~

You can easily add headers:

    >>> from http import Request
    >>> request = Request('GET', 'http://lumberjaph.net')
    >>> request.header('Connection', 'keep-alive')
    >>> print request.header('Connection')
    keep-alive
    
You can read more about headers in the *Headers* section.

Helpers
~~~~~~~

    >>> from http import Request
    >>> request = Request('GET', 'http://google.com')
    >>> request.header('If-Modified-Since', 'Wed, 08 Feb 2012 05:08:50 GMT')
    >>> request.if_modified_since
    datetime.datetime(2012, 2, 8, 5, 8, 50)

Is equivalent to:

    >>> request.if_modified_since = 'Wed, 08 Feb 2012 05:08:50 GMT'
    >>> request.if_modified_since
    datetime.datetime(2012, 2, 8, 5, 8, 50)
    >>> request.header('If-Modified-Since')
    'Wed, 8 Feb 2012 5:08:50 GMT'
    
The list of date helpers are:

#. ``if_modified_since``
#. ``if_unmodified_since``

This two helpers accept a date as a string or a class:``datetime`` object.

Response
--------

    >>> from http import Response
    >>> response = Response(200)
    
``Response`` is a class encapsulating HTTP style response, consisting of a response line, some headers and a content body.

Headers
~~~~~~~

    >>> response = Response(200, headers=[('Content-Type', 'application/json')])
    >>> response.header('Content-Type')
    'application/json'

Helpers
~~~~~~~

Headers
-------

``Headers`` is a class encapsulating HTTP Message headers.

Basic
~~~~~

    >>> from http import Headers
    >>> headers = Headers()
    >>> headers.add('Content-Type', 'application/json')
    >>> print headers.get('Content-Type')
    application/json
    >>> print headers
    Content-Type: application/json

Multi
~~~~~

    >>> headers = Headers()
    >>> headers.add('X-Custom', 'foo', 'bar')
    >>> headers.get_all('X-Custom')
    ['foo', 'bar']

Is equivalent to:

    >>> headers = Headers()
    >>> headers.add('X-Custom', 'foo')
    >>> headers.add('X-Custom', 'bar')
    >>> headers.get_all('X-Custom')
    ['foo', 'bar']

Helpers
~~~~~~~

    >>> h = Headers([('Content-Type', 'application/json')])
    >>> h.content_type
    'application/json'

    >>> headers = Headers()
    >>> headers.last_modified = datetime(2011, 12, 1, 0, 0)
    >>> print type(headers.last_modified)
    <type 'datetime.datetime'>

Url
---

HTTPException
-------------