from unittest2 import TestCase
from http import Response, Request, Url
from datetime import datetime


class TestClient(TestCase):

    def test_base(self):
        response = Response(status=200, message='OK')
        self.assertTrue(response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.message, 'OK')
        self.assertEqual(response.status_line, '200 OK')

        response = Response(status='200', message='OK')
        self.assertEqual(response.status, 200)

    def test_request(self):
        request = Request('GET', 'http://foobar')
        response = Response(status=200, message='OK', headers={},
                request=request)
    
    def test_base_url(self):
        response = Response(status=200, message='OK',
                headers={'Content-Base':'http://foo'})
        self.assertEqual(response.base, 'http://foo/')
        self.assertIsInstance(response.base, Url)

        response = Response(status=200, message='OK',
                headers={'Content-Location':'http://bar'})
        self.assertEqual(response.base, 'http://bar/')
        self.assertIsInstance(response.base, Url)

        request = Request('GET', 'http://baz')
        response = Response(status=200, message='OK', request=request)
        self.assertEqual(response.base, 'http://baz/')
        self.assertIsInstance(response.base, Url)

        response = Response(status=200)
        self.assertEqual(response.base, None)

    def test_date(self):
        response = Response(status=200, message='OK',
                headers={'Last-Modified':'Sat, 02 Jul 2011 07:53:00 GMT'})
        self.assertTrue(response.last_modified)
        self.assertIsInstance(response.last_modified, datetime)

    def test_content(self):
        response = Response(status=200, message='OK',
                headers={'Content-Type':'text/plain'})
        self.assertTrue(response.content_is_text)
        
        response.content = 'foo'
        self.assertTrue(response.content, 'foo')
