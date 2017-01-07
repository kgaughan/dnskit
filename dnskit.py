"""
dnskit - DNS without the pain.
"""

__version__ = '0.0.1'


def name(name_):
    return _Name(name_.split('.'))


class _Name:

    def __init__(self, labels):
        self.labels = labels

    @property
    def parent(self):
        return _Name(self.labels[1:])

    def query(self, rdtype, nameservers=None):
        return None

    def __str__(self):
        return '.'.join(self.labels)
