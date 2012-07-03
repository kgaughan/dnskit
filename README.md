dnskit
======

Here's the kind of thing I'm planning to aim for:

    import dnskit
    
    name = dnskit.name('example.com')
    registry_nss = name.parent.query(rdtype='NS')
    print name.query(rdtype='NS', nameservers=registry_nss)

That bit of code would query the registry's nameservers for the nameservers
associated with a given domain. Straightforward, no fuss.

Initially, it'll be a wrapper around dnspython, but if I'm feeling sufficiently
insane, I'll replace the low-level infrastructure with something dnskit specific.