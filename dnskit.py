"""
dnskit - DNS without the pain.
"""

import functools
import random

from dns import resolver as _r
from dns import rdatatype as _rdt


__version__ = '0.0.1'


def name(name_):
    return _Name(name_.split('.'))


def _get_resolver(nameservers):
    """
    :param list nameservers: Nameservers to use, nor None for default.
    :return: A resolver.
    :rtype: dns.resolver.Resolver
    """
    # If We're receiving a list of nameservers from a previous query, we
    # extract the naeserver names from the answer.
    if isinstance(nameservers, _r.Answer):
        nameservers = tuple(answer.target
                            for answer in nameservers
                            if answer.rdtype == _rdt.NS)
    if isinstance(nameservers, (list, tuple)):
        nameservers = tuple(sorted(str(host) for host in nameservers))
    print(nameservers)
    return _get_resolver_int(nameservers)


@functools.lru_cache(maxsize=64)
def _get_resolver_int(nameservers):
    """
    :param list nameservers: Nameservers to use, nor None for default.
    :return: A resolver.
    :rtype: dns.resolver.Resolver
    """
    if nameservers is None:
        return _r.get_default_resolver()
    resolver = _r.Resolver(configure=False)
    # We choose a single nameserver randomly and get its addresses.
    resolver.nameservers = _get_ns_addresses(random.choice(nameservers))
    return resolver


def _get_ns_addresses(ns):
    addresses = []
    ns_res = _r.get_default_resolver()
    for rdtype in (_rdt.AAAA, _rdt.A):
        for answer in ns_res.query(ns, rdtype, raise_on_no_answer=False):
            if answer.rdtype in (_rdt.AAAA, _rdt.A):
                addresses.append(answer.address)
    print(ns, addresses)
    return addresses


class _Name:

    def __init__(self, labels):
        self.labels = labels

    @property
    def parent(self):
        return _Name(self.labels[1:])

    def query(self, rdtype, nameservers=None):
        if isinstance(rdtype, str):
            rdtype = _rdt.from_text(rdtype)
        return _get_resolver(nameservers).query(str(self), rdtype)

    def __str__(self):
        return '.'.join(self.labels)
