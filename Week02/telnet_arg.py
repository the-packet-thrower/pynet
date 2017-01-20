#!usr/bin/env python

import telnetlib
import time
import sys
import socket

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    cmd = cmd.strip()
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + "\n")
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + "\n")
    return output

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection Timed Out")

def main():
    ip_addr = ['184.105.247.70','184.105.247.71']
    username = 'pyclass'
    password = '88newclass'

    for ip in ip_addr:
        remote_conn = telnet_connect(ip)
        output = login(remote_conn, username, password)
        output = send_command(remote_conn, "terminal length 0")
        output = send_command(remote_conn, sys.argv[1])
        print output

    remote_conn.close()




if __name__ == "__main__":
    main()

