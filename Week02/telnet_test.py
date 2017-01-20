#!usr/bin/env python

import telnetlib
import time
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    cmd = cmd.strip()
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    return remote_conn.read_very_eager()


def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)

    remote_conn.write(username + "\n")

    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + "\n")

    output = send_command(remote_conn, "terminal length 0")
    output = send_command(remote_conn, sys.argv[1])
    print output

    remote_conn.close()




if __name__ == "__main__":
    main()

