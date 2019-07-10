from unittest2 import TestCase
from http import Headers
from datetime import datetime


class TestHeaders(TestCase):

    ct_headers = (
        'Content-Type', 'application/json'
    )

    def test_simple(self):
        headers = Headers([self.ct_headers])
        self.assertTrue(headers)
        self.assertEqual(headers.content_type, 'application/json')

    def test_normalization(self):
        headers = Headers([self.ct_headers])

        self.assertTrue(headers.get('Content-Type'))
        self.assertTrue(headers.get('content-type'))
        self.assertEqual(headers.get('content-type'), 'application/json')

        headers.add('User-Agent', 'fluffy')
        self.assertTrue(headers.get('User-Agent'))
        self.assertTrue(headers.get('user-agent'))
        self.assertEqual(headers.get('user-agent'), 'fluffy')
        
    def test_remove(self):
        headers = Headers([self.ct_headers])
        headers.remove('Content-Type')
        ct = headers.content_type
        self.assertFalse(ct)

    def test_multi(self):
        headers = Headers()
        self.assertTrue(headers)

        headers.add('X-Foo', 'bar')
        headers.add('X-Foo', 'baz')
        
        self.assertEqual(headers.get('X-Foo'), 'bar')
        self.assertEqual(headers.get_all('X-Foo'), ['bar', 'baz'])

        headers = Headers()
        headers.add('X-Foo', 'bar', 'baz', 'foo')
        self.assertEqual(headers.get_all('X-Foo'), ['bar', 'baz', 'foo'])
        self.assertEqual(headers.get_all('x-fOo'), ['bar', 'baz', 'foo'])

    def test_content(self):
        headers = Headers([self.ct_headers])
        self.assertFalse(headers.content_is_text)

        def test_ct(ct, should_be):
            headers.remove('Content-Type')
            headers.add('Content-Type', ct)
            method = getattr(headers, should_be)
            self.assertTrue(method)

        test_ct('application/json', 'content_is_json')
        test_ct('text/html', 'content_is_text')
        test_ct('application/xhtml+xml', 'content_is_xhtml')
        test_ct('text/xml', 'content_is_xml')
        test_ct('application/xml', 'content_is_xml')
        test_ct('application/xhtml+xml', 'content_is_xml')
        test_ct('application/xhtml+xml; charset=UTF-8', 'content_is_xml')

    def test_content_params(self):
        headers = Headers({'Content-type': 'text/html; charset=UTF-8'})
        self.assertEqual(headers.content_type_params, {'charset': 'UTF-8'})
        headers = Headers({'Content-type': 'text/html'})
        self.assertEqual(headers.content_type_params, {})

    def test_date_header(self):
        headers = Headers([self.ct_headers])
        now = datetime(2011, 12, 12, 12, 0, 0)
        headers.if_unmodified_since = now
        self.assertEqual(headers.if_unmodified_since.year, now.year)
        self.assertEqual(headers.get('If-Unmodified-Since'), 'Mon, 12 Dec 2011 12:00:00 GMT')

        headers.if_modified_since = 'Mon, 12 Dec 2011 12:00:00 GMT'
        self.assertEqual(headers.if_modified_since.year, now.year)

    def test_str(self):
        headers = Headers([self.ct_headers])

    def test_iteritems(self):
        headers = Headers([self.ct_headers])

    def test_set(self):
        headers = Headers()
        headers.add('Content-Type', 'application/json')
        headers.set('Content-Type', 'application/xml')
        self.assertEqual(headers.get('Content-Type'), 'application/xml')

        headers = Headers()
        headers.set('Content-Type', 'application/xml')
        self.assertEqual(headers.get('Content-Type'), 'application/xml')
