dnskit
======

Here's the kind of thing I'm planning to aim for::

    import dnskit

    name = dnskit.name('example.com')
    registry_nss = name.parent.query(rdtype='NS')
    print(name.query(rdtype='NS', nameservers=registry_nss))

That bit of code would query the registry's nameservers for the nameservers
associated with a given domain. Straightforward, no fuss.

Initially, it'll be a wrapper around dnspython__, but if I'm feeling
sufficiently insane, I'll replace the low-level infrastructure with something
dnskit specific.

.. __: http://www.dnspython.org/

Compatibility
-------------

I'm only aiming for this to be Python 3 compatible. As dnspython supports
Python 3.3+, that's my baseline. I may support Python 2.7 if I have a pressing
personal necessity to support it, but as of now, it's not a priority.

Packaging is done with flit__ because I want to make my life easy, and wheels
are better in almost every way.

.. __: https://github.com/takluyver/flit
