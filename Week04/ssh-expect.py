#!/usr/bin/env python

import pexpect
import sys
import re

def main():
    pynet_rtr1 = '184.105.247.70'
    pynet_rtr2 = '184.105.247.71'
    username = 'pyclass'
    password = '88newclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, pynet_rtr1, port))
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('#')

    ssh_conn.expect('#')
    ssh_conn.sendline('show ip int br')
    ssh_conn.expect('#')
    #print ssh_conn.before
    #print ssh_conn.after

    #ssh_conn.sendline('show version')
    #ssh_conn.expect('#')
    #print ssh_conn.before
    
    
    try:
        ssh_conn.sendline('show version')
        ssh_conn.expect('zzzz')
    except pexpect.TIMEOUT:
        print "Found timeout"
   

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print ssh_conn.after

if __name__ == "__main__":
    main()
