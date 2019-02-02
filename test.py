import unittest

import dnskit


class TestName(unittest.TestCase):

    def test_basics(self):
        name = dnskit.name('example.com')
        self.assertIsInstance(name, dnskit._Name)
        self.assertEqual(name.labels, ['example', 'com'])
        self.assertEqual(str(name), 'example.com')

    def test_parent(self):
        name = dnskit.name('example.com')
        parent = name.parent
        self.assertIsInstance(parent, dnskit._Name)
        self.assertEqual(parent.labels, ['com'])
        self.assertEqual(str(parent), 'com')

class TestResolve(unittest.TestCase):

    def test_resolve(self):
        name = dnskit.name('talideon.com')
        response = name.query('NS')
        print([(answer, type(answer)) for answer in response])
        registry_nss = name.parent.query('NS')
        response = name.query('NS', nameservers=registry_nss)
        print([(answer, type(answer)) for answer in response])
