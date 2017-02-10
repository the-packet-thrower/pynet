#!/usr/bin/env python

'''
Use PExpect to do 'show ip int br'
'''

import pexpect
import time
from getpass import getpass


def login(ssh_conn):

    '''Handle sending password'''
    password = '88newclass'
    
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')

def find_prompt(ssh_conn):
    '''
    Find current prompt
    '''
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()

def main():
    '''
    Use PExpect for stuff
    '''
    ip_addr = raw_input("Enter IP address: ")
    username = 'pyclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3

    login(ssh_conn)
    prompt= find_prompt(ssh_conn)

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show ip int br')
    ssh_conn.expect(prompt)

    print '\n>>>>'
    print ssh_conn.before
    print '>>>>\n'

if __name__ == "__main__":
    main()
