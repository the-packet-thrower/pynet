#!/usr/bin/env python

import getpass
import snmp_helper
SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
    ip_addr1 = '184.105.247.70'
    ip_addr2 = '184.105.247.71'
    community_string = 'galileo'
    pynet_rtr1 = (ip_addr1, community_string, 161)
    pynet_rtr2 = (ip_addr2, community_string, 161)

    for a_device in (pynet_rtr1,pynet_rtr2):
        print "\n***************"
        for the_oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
            output = snmp_helper.snmp_extract(snmp_data)
            print output
    print "*************"


if __name__ == "__main__":
    main()
