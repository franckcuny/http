http a HTTP library for Python
==============================

http is heavily inspired by the `HTTP::Message <https://metacpan.org/module/HTTP::Message>`__ distribution.

Note
----

This repo was created to preserve the history of https://pypi.org/project/http/
it was manually re-created by downloading the history of sdists.
This repo is not currently owned, operated or endorsed by Franck Cuny

Synopsis
--------

    >>> from http import Request
    >>> request = Request('GET', 'http://pypi.python.org')
    >>> print request.method
    GET

Components
----------

http provides a few components to build HTTP messages:

- Headers: a class to manipulates HTTP headers
- Request: a class to encapsulate a HTTP request
- Response: a class to encapsulate a HTTP response
- Date: a class to convert date to and from ISO 8601 
- Url: a class to manipulate url

Headers
~~~~~~~

    >>> from http import Headers
    >>> h = Headers()
    >>> h.add('Content-Type', 'application/json')

Request
~~~~~~~

    >>> from http import Request
    >>> r = Request('GET', 'htttp://lumberjaph.net')

Response
~~~~~~~~

    >>> from http import Response
    >>> r = Response(200)

Links
-----

- `Documentation <http://readthedocs.org/docs/http/en/latest/>`__.
- `Repository <git://github.com/franckcuny/http.git>`__.

How to get?
-----------

At the moment, the only way to get http is by checking out the development version.

I also recommend to use `virtualenv <https://pypi.org/project/virtualenv/>`__ and `pip <https://pypi.org/project/pip/>`__ to work with this repository.

To get the sources and install all the requirements:

```
    $ pip install http
    $ git clone git://github.com/franckcuny/http.git
    $ cd http
    $ virtualenv env
    $ source virtualenv/bin/activate
    $ pip install -r requirements-test.txt
```
