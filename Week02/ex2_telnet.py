import telnetlib
import sys
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6
IP_ADDR = '184.105.247.70'
USERNAME = 'pyclass'
PASSWORD = '88newclass'

def main():
    remote_conn = telnetlib.Telnet(IP_ADDR,TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername",TELNET_TIMEOUT)
    remote_conn.write(USERNAME + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(PASSWORD + '\n')

    remote_conn.write("terminal length 0" + "\n")
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.write("show ip int br" + "\n")

    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()
