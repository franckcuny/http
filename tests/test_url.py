from unittest2 import TestCase
from http import Url
from itertools import product

class Test_Url(TestCase):
    flavours = (
        {   'absolute': ('http://example.com', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('host', lambda u: u.host=='example.com'),
                        ('netloc', lambda u: u.netloc=='example.com'),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),
            'relative': ('', (
                        ('is_absolute', lambda u: not u.is_absolute),
                        ('is_relative', lambda u: u.is_relative),
                        ('host', lambda u: u.host is None),
                        ('netloc', lambda u: u.netloc==''),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),
            'secure':   ('https://example.org', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('is_secure', lambda u: u.is_secure),
                        ('host', lambda u: u.host=='example.org'),
                        ('netloc', lambda u: u.netloc=='example.org'),
                        ('username', lambda u: not u.username),
                        ('password', lambda u: not u.password),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: u.is_secure),
                        )),
            'auth_w_pass': ('http://toto:pass@example.org', (
                        ('is_absolute', lambda u: u.is_absolute),
                        ('is_relative', lambda u: not u.is_relative),
                        ('host', lambda u: u.host=='example.org'),
                        ('netloc', lambda u: u.netloc=='toto:pass@example.org'),
                        ('username', lambda u: u.username == 'toto'),
                        ('password', lambda u: u.password == 'pass'),
                        ('port', lambda u: u.port is None),
                        ('is_secure', lambda u: not u.is_secure),
                        )),

        },
        {   ' root': ('/', (
                    ('path', lambda u: u.path == ['']),
                    )),
            ' w_path': ('/foo/bar/wib.ble', (
                    ('path', lambda u: u.path == ['', 'foo', 'bar', 'wib.ble']),
                    )),
        },
        {   ' vanilla': ( '', (
                       ('query', lambda u: u.query == []),
                       )),
            ' w_query': ('?a=b&a=c&d=e', (
                       ('query', lambda u: u.query == [('a', 'b'), ('a', 'c'), ('d', 'e')]),
                       )),
        }
    )

    def url_flavours(self):
        allitems = [ x.iteritems() for x in self.flavours ]
        return product(*allitems)

    def test_init(self):
        flavours = self.url_flavours()
        for f in flavours:
            msg = reduce(lambda a, b: a+b[0], f, '')
            urlstr = reduce(lambda a, b: a+b[1][0], f, '')
            tests = reduce(lambda a, b: a+b[1][1], f, tuple())
            url = Url(urlstr)
            for tname, predicate in tests:
                self.assertTrue(predicate(url), msg=msg+": "+tname)
            copy = Url(str(url))
            self.assertEqual(str(copy), str(url), msg="copy is not identical")

    def test_netloc(self):
        u=Url()
        self.assertTrue(u)
        u.username = 'toto'
        u.password = 'pass'
        u.host = 'foob.ar'
        self.assertEqual('toto:pass@foob.ar', u.netloc)
        self.assertEqual(None, u.port)
        u.netloc = 'toto.com'
        self.assertEqual(None, u.username)
        self.assertEqual(None, u.password)
        self.assertEqual('toto.com', u.host)
        self.assertEqual(None, u.port)

    def test_add(self):
        u = Url('https://foob.ar/some/where/some/thing')
        a = Url('http://foob.it/')
        rel = Url('../../rville')
        self.assertEqual(a, u+a)
        self.assertEqual(u, a+u)
        self.assertEqual(Url('https://foob.ar/some/rville'), u+rel)
        self.assertEqual(u, rel+u)

    def test_path_append(self):
        u = Url(host='foo.com', scheme='http')
        u.path.append('foo')
        u.path.append('bar')
        self.assertTrue(str(u), 'http://foo.com/foo/bar')

        u = Url(host='foo.com', scheme='http')
        u.path.append('foo/bar')
        self.assertEqual(len(u.path), 2)
        self.assertEqual(u.path[0], 'foo')
        self.assertEqual(u.path[1], 'bar')
        self.assertTrue(str(u), 'http://foo.com/foo/bar')
        
    def test_final_slash(self):
        u = Url(host='foo.com', scheme='http')
        self.assertEqual(u, 'http://foo.com/')
        
        u = Url('http://foo.com')
        self.assertEqual(u, 'http://foo.com/')
        
    def test_path_unicode(self):
        u = Url(host='foo.com', scheme='http')
        u.path.append(unicode('/foo/bar/baz'))
        self.assertEqual(len(u.path), 4)
        self.assertEqual(str(u), 'http://foo.com/foo/bar/baz')