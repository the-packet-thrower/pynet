import telnetlib
import time

if __name__ == "__main__":

    ip = '184.105.247.70'
    username = 'admin'
    password = 'dikstra'
    DELAY = time.sleep(1)

    TELNET_PORT = 23
    TELNET_TIMEOUT = 6
    READ_TIMEOUT = 6

    remote_conn = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", READ_TIMEOUT)
    remote_conn.write(username + "\n")
    output = remote_conn.read_until("ssword:", READ_TIMEOUT)
    remote_conn.write(password + "\n")

    remote_conn.write("terminal length 0\n")
    DELAY
    output = remote_conn.read_very_eager()

    remote_conn.write("\n")
    remote_conn.write("show version\n"

    output = remote_conn.read_very_eager()
    print output
