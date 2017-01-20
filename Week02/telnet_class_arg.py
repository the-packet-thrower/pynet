#!usr/bin/env python

import telnetlib
import time
import sys
import socket
import pprint

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class TelnetConn(object):
    ''' 
    Telnet Class
    '''
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        
        try:
            self.remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection Timed Out")
    
    def send_command(self, cmd=sys.argv[1], sleep_time=1):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)
        return self.remote_conn.read_very_eager()

    def login(self):
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + "\n")
        output += self.remote_conn.read_until("assword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + "\n")
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output
        '''
        return self.send_command(paging_cmd)
 

    def close_conn(self):
        '''
        Close telnet connection
        '''
        self.remote_conn.close()

def main():
    ip_addr = ['184.105.247.70','184.105.247.71']
    username = 'pyclass'
    password = '88newclass'
    
    for ip in ip_addr:
        my_conn = TelnetConn(ip, username, password)
        my_conn.login()
        my_conn.disable_paging()
        output = my_conn.send_command()
        print output 

    my_conn.close_conn()

if __name__ == "__main__":
    main()
